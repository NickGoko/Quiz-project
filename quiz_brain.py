class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        """This will access the question_bank in the main.py file and 
        question_number is the index for the number question inside the question_bank
        This basically a way to format the code to read Q. 1 the question
        And set up current_question number so that the next part doesn't need to say current_question.self.question_number
        or something like that. The index or number question is already set up"""
        self.question_number += 1
        user_answer= input(f" Q. {self.question_number} : {current_question.text} (True or False)")
        """ current_question.text displays the question without the answer which was saved in the question_bank made of
        the question_text and question_answer then passed over into the Question class which needs text and 
        answer parameter with object being new_question that is stored in list of question_bank """
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got that right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/ {self.question_number}")
        print()


