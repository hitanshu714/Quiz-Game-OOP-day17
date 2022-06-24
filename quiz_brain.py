class QuizBrain:
    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        user_answer = input(f"Q. {self.question_no+1}: {current_question.text} (True/False): ").lower()
        self.question_no += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, current_ans):
        correct_ans = current_ans.lower()
        if user_ans == correct_ans:
            self.score += 1
            print("Correct!")
            return True
        else:
            print(f"Wrong...")
            return False


