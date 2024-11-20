def quiz():
    print("Welcome to the Python Quiz! 🎉")
    score = 0

    questions = [
        {
            "question": "What is the correct way to create a function in Python?",
            "options": ["A. function myFunction()", "B. def myFunction():", "C. create myFunction()"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to create a loop in Python?",
            "options": ["A. repeat", "B. for", "C. loop"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a mutable data type in Python?",
            "options": ["A. tuple", "B. string", "C. list"],
            "answer": "C"
        },
        {
            "question": "Which built-in function is used to get the length of a string in Python?",
            "options": ["A. count()", "B. len()", "C. length()"],
            "answer": "B"
        }, 
        {
            "question": "What does 'print()' function do in Python? ",
            "options": ["A. Outputs data to the console", "B. Prints a document", "C. Executes code"],
            "answer": "A"
        }
    ]

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Choose the correct answer (A, B, or C): ").upper()

        if answer == q["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print("Wrong answer. 😞")

    print(f"\nYour final score is: {score}/{len(questions)}")

    # Option to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        quiz()
    else:
        print("Thanks for playing! Goodbye! 👋")

# Start the quiz
quiz()
