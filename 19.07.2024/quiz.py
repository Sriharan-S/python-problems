def ask_question(question, options, correct_answer):
    """Ask a single multiple-choice question and return if the answer is correct."""
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        answer = int(input("Enter the number of your choice: "))
        if options[answer - 1] == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
            return False
    except (IndexError, ValueError):
        print("Invalid choice. Please enter a number corresponding to one of the options.")
        return False

def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_answer": "4"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Mars"
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Welcome to the Quiz!")
    
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1
    
    print(f"\nQuiz Finished! Your score: {score}/{total_questions}")

quiz()
