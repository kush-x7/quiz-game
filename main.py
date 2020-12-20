from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dic in question_data:
    question_text = dic["text"]
    question_answer = dic["answer"]

    # created obj of class question
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you've completed the quiz")
print(f"Your final score was: {quiz.score}/ {len(question_bank)}")
