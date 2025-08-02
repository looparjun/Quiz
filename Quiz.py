import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris",
        "hint": "It's known for the Eiffel Tower."
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "12", "14", "15"],
        "answer": "12",
        "hint": "It's more than 11."
    },
    {
        "question": "What is the color of the sky?",
        "options": ["Green", "Blue", "Red", "Yellow"],
        "answer": "Blue",
        "hint": "Think of a clear day."
    }
]

score = 0
hints_left = 3

print("🎮 Welcome to the Quiz Game!\n")

random.shuffle(questions)

for q in questions:
    print(f"Q: {q['question']}")
    for i, opt in enumerate(q["options"], start=1):
        print(f"   {i}. {opt}")

    use_hint = input("Do you want a hint? (yes/no): ").strip().lower()
    if use_hint == "yes" and hints_left > 0:
        print(f"Hint: {q['hint']}")
        hints_left -= 1
        print(f"Hints left: {hints_left}")
    elif use_hint == "yes":
        print("❌ No hints left.")

    answer = input("Enter your answer (1-4): ").strip()
    try:
        index = int(answer) - 1
        if q["options"][index] == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q['answer']}\n")
    except:
        print("⚠️ Invalid input. Moving to next question.\n")

print(f"🏁 Game Over! Your score: {score}/{len(questions)}")
