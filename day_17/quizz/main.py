from question_model import Question
from data import question_data
from quizz_brain import QuizBrain

question_bank =[]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


quizz = QuizBrain(question_bank)
while quizz.still_has_question():

    quizz.next_question()
print("you have completed quizz")
print(f"your total score is {quizz.score}/{quizz.question_number}")