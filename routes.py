def get_filtered_questions(quiz_id, mode, level):
    quiz = quizzes.get(quiz_id)
    questions = quiz["questions"]

    # Filter Level
    filtered = [q for q in questions if q["level"] == level]

    # Filter Mode
    if mode == "mcq":
        filtered = [q for q in filtered if q["type"] == "mcq"]
    elif mode == "essay":
        filtered = [q for q in filtered if q["type"] == "essay"]

    return filtered
