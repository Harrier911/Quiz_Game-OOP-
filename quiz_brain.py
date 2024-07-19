
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list
    def still_has_questions(self):
        self.number_of_questions = len(self.questions_list)
        if self.question_number < self.number_of_questions:
            return True
        else:
            return False
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (T/F)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")

        print(f"The correct answer was {correct_answer}")
        print(f"Your score is ({self.score}/{self.question_number})")
        print("\n")




