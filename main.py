class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def conduct_quiz(self):
        print("Welcome to the Quiz!\n")

        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.text}")
            for j, option in enumerate(question.options, 1):
                print(f"{j}. {option}")

            user_answer = int(input("Your answer (enter the option number): "))

            if question.is_correct(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was option {question.correct_option}.\n")

        print(f"Quiz completed! Your score is: {self.score}/{len(self.questions)}")


question1 = Question("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], 1)
question2 = Question("Which programming language is this quiz written in?", ["Python", "Java", "C++", "JavaScript"], 1)
question3 = Question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Venus"], 2)


quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)


quiz.conduct_quiz()