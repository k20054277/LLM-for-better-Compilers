
# Define a dictionary for storing answers and their corresponding correct values
answers = {
    "What is the smallest number in the set {0, 1, 5, 7, 9}?": False,
    "What is the result of adding 2 and 3?": (2, 3, 5),
    "Which number is odd among these {4, 6, 9}?": False,
    "What is the sum of 7 and 3?": 10,
    "Which number is even among these {1, 4, 8}?": True
}

# Function to check user's answer and return result
def check_answer(question, user_answer):
    correct_answer = answers[question]
    if type(correct_answer) is bool:
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print("Incorrect.")
    elif type(correct_answer) is list:
        if user_answer in correct_answer:
            print("Correct!")
        else:
            print("Incorrect.")
    else:
        if user_answer == correct_answer:
            print(f"Correct! The answer is {correct_answer}")
        else:
            print(f"Incorrect. The answer is {correct_answer}")

# Quiz the user with questions and check their answers
questions = [
    "What is the smallest number in the set {0, 1, 5, 7, 9}?",
    "What is the result of adding 2 and 3?",
    "Which number is odd among these {4, 6, 9}?",
    "What is the sum of 7 and 3?",
    "Which number is even among these {1, 4, 8}?"
]

for i in range(len(questions)):
    print(f"Question {i+1}: {questions[i]}")
    user_answer = input("Your answer: ")
    check_answer(questions[i], user_answer)
