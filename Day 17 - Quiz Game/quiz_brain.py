class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # returns True or False

    def check_answer(self, user_ans, correct_ans):
        """Checks if answer entered by user is equal to the correct answer."""
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("The answer is correct.")
        else:
            print("The answer is wrong.")
        print("The correct answer was:", correct_ans)
        print("Your current score is:", self.score, "/", self.question_number, "\n---\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number} - {current_question.text} (True/False)?: ")
        self.check_answer(user_ans, current_question.answer)
