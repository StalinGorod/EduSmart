from flask import (
    Flask,
    render_template,
    request,
    abort,
    flash,
    redirect,
    url_for,
    session,
    render_template_string,
)
from lesson_data import LESSONS
from models import QuizModel
from collections import defaultdict
import random
from flask_session import Session
import os
import difflib
import spacy
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from datetime import datetime

app = Flask(__name__)
app.secret_key = "6efa30342818ff2e989e6097459c19124a600564f51dc373"

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = os.path.join(os.getcwd(), "flask_session")
app.config["SESSION_PERMANENT"] = False
Session(app)

factory = StemmerFactory()
stemmer = factory.create_stemmer()
nlp = spacy.load("xx_ent_wiki_sm")


def get_similarity(word1, word2):
    return nlp(word1).similarity(nlp(word2))


def get_all_quizzes():
    pass


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/lesson/<lesson_id>")
def lesson_detail(lesson_id: str):
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        abort(404)
    selected_type = request.args.get("type", "video")
    available_types = [res["type"] for res in lesson.get("resources", [])]

    if selected_type not in available_types:
        selected_type = "video"

    return render_template(
        "lesson.html",
        lesson=lesson,
        selected_type=selected_type,
    )


@app.route("/save-notes/<lesson_id>", methods=["POST"])
def save_notes(lesson_id):
    flash("Your notes have been submitted successfully!")
    return redirect(url_for("lesson_detail", lesson_id=lesson_id, type="notes"))


@app.route("/video")
@app.route("/video/<subject_slug>")
def video_library(subject_slug=None):
    subject_map = {
        "mathematics": "Mathematics",
        "science-physics": "Science & Physics",
        "english-linguistics": "English & Linguistics",
        "computer-science-it": "Computer Science & IT",
        "social-studies-history": "Social Studies & History",
    }
    selected_subject = subject_map.get(subject_slug)

    # Filter data
    if selected_subject:
        all_filtered = [
            l for l in LESSONS.values() if l["subject_label"] == selected_subject
        ]
    else:
        all_filtered = list(LESSONS.values())

    # Pagination Logic
    per_page = 16
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * per_page
    end = start + per_page

    lessons_to_show = all_filtered[start:end]
    total_pages = (len(all_filtered) + per_page - 1) // per_page or 1

    return render_template(
        "video.html",
        lessons=lessons_to_show,
        current_subject=subject_slug,
        current_page=page,
        total_pages=total_pages,
    )


@app.route("/video/play/<lesson_id>")
def play_video(lesson_id):
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        abort(404)
    return render_template("video_player.html", lesson=lesson)


@app.route("/quiz", defaults={"quiz_id": None}, methods=["GET", "POST"])
@app.route("/quiz/<quiz_id>", methods=["GET", "POST"])
def quiz_index(quiz_id):
    # 1. HALAMAN DAFTAR KUIS
    if quiz_id is None:
        all_quizzes = QuizModel.get_all()
        grouped_quizzes = defaultdict(list)
        for q_id, q_data in all_quizzes.items():
            subject = q_data.get("subject", "General")
            grouped_quizzes[subject].append((q_id, q_data))
        subjects = sorted(list(grouped_quizzes.keys()))
        return render_template(
            "quiz.html", grouped_quizzes=grouped_quizzes, subjects=subjects, quiz=None
        )

    # 2. LOGIKA KUIS
    quiz = QuizModel.get_by_id(quiz_id)
    if not quiz:
        abort(404)

    raw_questions = quiz.get("questions", [])
    all_questions = list(raw_questions)
    session_key = f"quiz_order_{quiz_id}"

    # 3. HANDLE SUBMIT (POST)
    if request.method == "POST":
        ordered_ids = session.get(session_key)
        if not ordered_ids:
            flash("Session expired.", "warning")
            return redirect(url_for("quiz_index"))

        id_map = {str(q["id"]): q for q in all_questions}
        current_questions = [id_map[str(qid)] for qid in ordered_ids]
        mode = request.args.get("mode")

        score, results = 0, []
        user_answers = request.form.to_dict()
        stop_words = {
            "dan",
            "atau",
            "yang",
            "dengan",
            "untuk",
            "adalah",
            "itu",
            "pada",
            "di",
            "ke",
            "dari",
        }

        for q in current_questions:
            if mode and q.get("type") != mode:
                continue

            ans = user_answers.get(str(q["id"]))
            if ans is not None:
                # Normalisasi ke kata dasar
                user_str = stemmer.stem(str(ans).strip().lower())
                correct_str = stemmer.stem(str(q.get("answer", "")).strip().lower())

                is_correct = False
                if q.get("type") == "essay":
                    keywords = [
                        w
                        for w in correct_str.split()
                        if len(w) >= 3 and w not in stop_words
                    ]

                    if not keywords:
                        is_correct = (
                            difflib.SequenceMatcher(None, user_str, correct_str).ratio()
                            >= 0.3
                        )
                    else:
                        found_count = 0
                        for kw in keywords:
                            if kw in user_str:
                                found_count += 1
                            else:
                                for u_word in user_str.split():
                                    if (
                                        len(u_word) >= 3
                                        and get_similarity(kw, u_word) >= 0.8
                                    ):
                                        found_count += 1
                                        break
                        is_correct = (found_count / len(keywords)) >= 0.5
                else:
                    is_correct = user_str == correct_str

                if is_correct:
                    score += 1
                results.append(
                    {
                        "question": q["text"],
                        "user": ans,
                        "correct": is_correct,
                        "correct_answer": q.get("answer"),
                        "expl": q.get("explanation", "No explanation."),
                    }
                )

        session["last_results"] = {
            "score": score,
            "total_answered": len(results),  # Kunci ini harus ada
            "total_all": len(current_questions),  # Kunci ini harus ada
            "results": results,
        }
        session.pop(session_key, None)
        return redirect(url_for("show_results"))

    # 4. RENDER HALAMAN KUIS (GET)
    if session_key not in session:
        random.shuffle(all_questions)
        session[session_key] = [q["id"] for q in all_questions]

    ordered_ids = session.get(session_key)
    id_map = {str(q["id"]): q for q in all_questions}
    filtered_quiz = dict(quiz)
    filtered_quiz["questions"] = [id_map[str(qid)] for qid in ordered_ids]

    return render_template("quiz.html", quiz=filtered_quiz, quiz_id=quiz_id)


@app.route("/quiz/results")
def show_results():
    data = session.get("last_results")
    if not data:
        flash("No quiz results found.", "warning")
        return redirect(url_for("quiz_index"))

    # FILTER: Hanya ambil soal yang memiliki jawaban (user tidak kosong/None)
    answered_results = [
        r
        for r in data["results"]
        if r.get("user") is not None and str(r["user"]).strip() != ""
    ]

    # Hitung jumlah soal yang dijawab (Attempted)
    actual_attempted = len(answered_results)

    return render_template(
        "results.html",
        score=data["score"],
        total_answered=actual_attempted,  # Ini sudah angka yang difilter
        total_all=data["total_all"],
        results=data[
            "results"
        ],  # Kirim semua untuk review, tapi gunakan filter di HTML
    )


@app.route("/progress")
def progress():
    return render_template("progress.html", now=datetime.now)


@app.route("/online")
def online():
    return render_template("online.html")


@app.route("/discuss")
def discuss():
    return render_template("discuss.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/reward")
def reward():
    return render_template("reward.html")


if __name__ == "__main__":
    # Pastikan folder flask_session ada
    if not os.path.exists("flask_session"):
        os.makedirs("flask_session")
    app.run(debug=True)
