import random

class QuizHandler:
    def __init__(self):
        self.questions = [
            {
                "question": "¿Cuál es la capital de Francia?",
                "answers": ["Berlín", "Madrid", "París", "Roma"],
                "correct": 2
            },
            {
                "question": "¿Cuál es la capital de España?",
                "answers": ["Lisboa", "Madrid", "París", "Roma"],
                "correct": 1
            },
            {
                "question": "¿Cuál es la capital de Italia?",
                "answers": ["Berlín", "Madrid", "París", "Roma"],
                "correct": 3
            },
            {
                "question": "¿Cuál es la capital de Alemania?",
                "answers": ["Berlín", "Madrid", "París", "Roma"],
                "correct": 0
            }
        ]
        self.current_question_index = -1
        self.current_answers = []
        self.current_question = ""

    def get_next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]["question"]
            self.current_answers = self.questions[self.current_question_index]["answers"]
        else:
            self.current_question = "¡Fin del juego!"
            self.current_answers = []

    def check_answer(self, answer_index):
        if self.current_question_index < len(self.questions):
            correct_index = self.questions[self.current_question_index]["correct"]
            return answer_index == correct_index
        return False
