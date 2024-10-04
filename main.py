from question_model import Question
from data import question_data
from quiz_brain import Answer


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Answer(question_bank)

while quiz.question_check():
    quiz.next_question()

print(f'All done! Your final score was {quiz.score}/{quiz.q_num}')