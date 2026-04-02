#PROJECT 4 :- Quiz Game
def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
            "answer": "A"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Mark Twain"],
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
            "answer": "A"
        }
    ]

    score = 0
    for index,question in enumerate(questions):
        print(f"Question {index + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")
        print()
    print(f"Your final score is: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz = True
    while run_quiz:
        quiz_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            run_quiz = False
            print("Thanks for playing!")

