class QuizBrain:
  def __init__(self, q_list):
    #q_list will be the question_bank in the main.py
    self.question_number = 0
    self.question_list = q_list
    self.score = 0

  def still_has_questions(self):
    if self.question_number == len(self.question_list):
      return False
    else:
      return True    

  
  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    # When written 'current_question.text', the 'text' is mentioned in the 'Class Question'.
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
    #question_answer = current_question.answer
    self.check_answer(user_answer, current_question.answer)
    #We don't need to put the above input into a variable

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      self.score += 1
      print("You got it right!")      
    else:      
      print("You are wrong.")      
      
    print(f"The correct answer was {correct_answer}")
    print(f"Your current score is {self.score}/{self.question_number}")
    print("\n")
    if self.question_number == len(self.question_list):
      print("\n")
      print("You have completed the quiz!")
      print(f"Your final score is {self.score}/{self.question_number}")
      
      
      