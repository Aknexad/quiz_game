from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


qustion_bank =[]
for qustion in question_data:
    qustion_txte = qustion["text"]
    qustion_answer = qustion["answer"]
    new_qustion = Question(qustion_txte,qustion_answer)

    qustion_bank.append(new_qustion)

quiz = QuizBrain(qustion_bank)


while quiz.still_has_question():
    quiz.next_qustion()

print("your are complit the quize")
    
print(f"your score is {quiz.score}/{len(qustion_bank)}  qustion ")


