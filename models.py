import json
import os


class QuizModel:

    FILE_PATH = "quiz.json"

    @classmethod
    def get_all(cls):
        """Membaca seluruh data kuis dari file JSON."""
        if not os.path.exists(cls.FILE_PATH):
            return {}
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error membaca file {cls.FILE_PATH}: {e}")
            return {}

    @classmethod
    def get_by_id(cls, quiz_id):
        """Mengambil data kuis spesifik berdasarkan ID."""
        return cls.get_all().get(quiz_id)
