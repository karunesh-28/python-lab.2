'''Create a Python program for an online quiz system. Implement classes for
quizzes, questions, and users. Include methods for taking quizzes, scoring, and
displaying results.'''

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.text)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        user_score = 0

        print(f"\n--- {self.name} ---")
        for question in self.questions:
            question.display_question()
            user_answer = int(input("Your answer (enter the option number): "))
            
            if question.is_correct(user_answer):
                print("Correct!\n")
                user_score += 1
            else:
                print("Incorrect. The correct answer was option", question.correct_option, "\n")

        print(f"{user.name}'s Quiz Score: {user_score}/{len(self.questions)}")
        return user_score


class User:
    def __init__(self, name):
        self.name = name

# Example usage:
# Create questions
question1 = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3)
question2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2)
question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 2)

# Create a quiz with the questions
quiz = Quiz("General Knowledge Quiz", [question1, question2, question3])

# Create a user
user = User("John")

# Take the quiz and display the result
quiz_result = quiz.take_quiz(user)
