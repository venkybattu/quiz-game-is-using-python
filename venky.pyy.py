import random

def run_quiz(questions):
    score = 0
    random.shuffle(questions)  # Shuffle questions each run

    for q in questions:
        print("\n" + q["question"])
        options = q["options"].copy()
        random.shuffle(options)  # Shuffle options for fairness

        # Display options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if options[choice-1].lower() == q["answer"].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except:
            print("Invalid input. Skipping question.")

    # Final result
    print("\n🎯 Quiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    # Grade system
    if percentage == 100:
        print("🏆 Excellent! Perfect Score!")
    elif percentage >= 70:
        print("👍 Good Job!")
    elif percentage >= 40:
        print("🙂 Keep Practicing!")
    else:
        print("😢 Needs Improvement.")


# Question Bank
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which programming language is mainly used for AI?",
        "options": ["Python", "C++", "Java", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["Charles Babbage", "Alan Turing", "Elon Musk", "Bill Gates"],
        "answer": "Charles Babbage"
    },
    {
        "question": "Which is the largest planet in our Solar System?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Which company developed the Windows OS?",
        "options": ["Apple", "Microsoft", "IBM", "Google"],
        "answer": "Microsoft"
    }
]

# Run the quiz
print("🎉 Welcome to the Python Quiz Game 🎉")
run_quiz(questions)