from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for i in question_data:
  question_text = i['question']
  question_answer = i['correct_answer']
  question = Question(question_text, question_answer)
  question_bank.append(question)
  
  
 
# here we are entering 'question_bank' into the 'q_list' in the QuizBrain class
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():  
  value = quiz.next_question()

  
  