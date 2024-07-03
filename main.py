'''
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","Arko")
user_2 = User("002", "Hasin")

# user_1.followers = 300
user_1.follow(user_2)
print(user_1.following)
'''

from question_model import *
from data import question_data
from quiz_brain import *

question_bank = []


for i in question_data:
    q = i.get("question")
    a = i.get("correct_answer")
    new_q = Question(q, a)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")