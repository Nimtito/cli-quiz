import random

questions = [
    {
        "question": "What does CPU stand for?",
        "choices": {
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Utility",
            "D": "Control Processing User"
        },
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": {
            "A": "function",
            "B": "func",
            "C": "def",
            "D": "define"
        },
        "answer": "C"
    },
    {
        "question": "What is the output of 5 + 3?",
        "choices": {
            "A": "53",
            "B": "8",
            "C": "15",
            "D": "2"
        },
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False values?",
        "choices": {
            "A": "String",
            "B": "Integer",
            "C": "Boolean",
            "D": "Float"
        },
        "answer": "C"
    },
    {
        "question": "Which loop is commonly used when the number of iterations is known?",
        "choices": {
            "A": "while",
            "B": "for",
            "C": "do while",
            "D": "repeat"
        },
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "choices": {
            "A": "//",
            "B": "/*",
            "C": "#",
            "D": "--"
        },
        "answer": "C"
    },
    {
        "question": "What is the correct way to create a list in Python?",
        "choices": {
            "A": "(1, 2, 3)",
            "B": "{1, 2, 3}",
            "C": "[1, 2, 3]",
            "D": "<1, 2, 3>"
        },
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from a user?",
        "choices": {
            "A": "print()",
            "B": "scan()",
            "C": "input()",
            "D": "read()"
        },
        "answer": "C"
    },
    {
        "question": "What is the output of len('Python')?",
        "choices": {
            "A": "5",
            "B": "6",
            "C": "7",
            "D": "8"
        },
        "answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "choices": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "String"
        },
        "answer": "C"
    }
]

# SHUFFLE QUESTIONS

random.shuffle(questions)

# QUIZ INTRODUCTION


print("=" * 50)
print("      WELCOME TO THE PYTHON QUIZ GAME")
print("=" * 50)

score = 0
question_number = 1

for question in questions:

    print(f"\nQuestion {question_number}")
    print(question["question"])

    # Display choices
    for option, choice in question["choices"].items():
        print(f"{option}. {choice}")

 # Input validation using try/except
    while True:
        try:
            user_answer = input("\nEnter your answer (A/B/C/D): ").upper()

            if user_answer not in ["A", "B", "C", "D"]:
                raise ValueError

            break

        except ValueError:
            print("Invalid input!")
            print("Please enter A, B, C, or D.")
 # Check answer
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {question['answer']}.")

    question_number += 1

# FINAL RESULTS

print("\n" + "=" * 50)
print("              QUIZ COMPLETE")
print("=" * 50)

print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.0f}%")


