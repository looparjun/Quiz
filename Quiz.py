
import random

questions = [{'question': 'What is 31 + 31?', 'options': ['61', '62', '63', '64'], 'answer': 1, 'hint': "It's double of 31."}, {'question': 'What is 25 + 25?', 'options': ['49', '50', '51', '52'], 'answer': 1, 'hint': "It's double of 25."}, {'question': 'What is 27 + 27?', 'options': ['53', '54', '55', '56'], 'answer': 1, 'hint': "It's double of 27."}, {'question': 'What is 28 + 28?', 'options': ['55', '56', '57', '58'], 'answer': 1, 'hint': "It's double of 28."}, {'question': 'What is 47 + 47?', 'options': ['93', '94', '95', '96'], 'answer': 1, 'hint': "It's double of 47."}, {'question': 'What is 9 + 9?', 'options': ['17', '18', '19', '20'], 'answer': 1, 'hint': "It's double of 9."}, {'question': 'What is 11 + 11?', 'options': ['21', '22', '23', '24'], 'answer': 1, 'hint': "It's double of 11."}, {'question': 'What is 4 + 4?', 'options': ['7', '8', '9', '10'], 'answer': 1, 'hint': "It's double of 4."}, {'question': 'What is 18 + 18?', 'options': ['35', '36', '37', '38'], 'answer': 1, 'hint': "It's double of 18."}, {'question': 'What is 43 + 43?', 'options': ['85', '86', '87', '88'], 'answer': 1, 'hint': "It's double of 43."}, {'question': 'What is 22 + 22?', 'options': ['43', '44', '45', '46'], 'answer': 1, 'hint': "It's double of 22."}, {'question': 'What is 35 + 35?', 'options': ['69', '70', '71', '72'], 'answer': 1, 'hint': "It's double of 35."}, {'question': 'What is 50 + 50?', 'options': ['99', '100', '101', '102'], 'answer': 1, 'hint': "It's double of 50."}, {'question': 'What is 29 + 29?', 'options': ['57', '58', '59', '60'], 'answer': 1, 'hint': "It's double of 29."}, {'question': 'What is 5 + 5?', 'options': ['9', '10', '11', '12'], 'answer': 1, 'hint': "It's double of 5."}, {'question': 'What is 34 + 34?', 'options': ['67', '68', '69', '70'], 'answer': 1, 'hint': "It's double of 34."}, {'question': 'What is 42 + 42?', 'options': ['83', '84', '85', '86'], 'answer': 1, 'hint': "It's double of 42."}, {'question': 'What is 3 + 3?', 'options': ['5', '6', '7', '8'], 'answer': 1, 'hint': "It's double of 3."}, {'question': 'What is 1 + 1?', 'options': ['1', '2', '3', '4'], 'answer': 1, 'hint': "It's double of 1."}, {'question': 'What is 49 + 49?', 'options': ['97', '98', '99', '100'], 'answer': 1, 'hint': "It's double of 49."}, {'question': 'What is 15 + 15?', 'options': ['29', '30', '31', '32'], 'answer': 1, 'hint': "It's double of 15."}, {'question': 'What is 36 + 36?', 'options': ['71', '72', '73', '74'], 'answer': 1, 'hint': "It's double of 36."}, {'question': 'What is 20 + 20?', 'options': ['39', '40', '41', '42'], 'answer': 1, 'hint': "It's double of 20."}, {'question': 'What is 24 + 24?', 'options': ['47', '48', '49', '50'], 'answer': 1, 'hint': "It's double of 24."}, {'question': 'What is 13 + 13?', 'options': ['25', '26', '27', '28'], 'answer': 1, 'hint': "It's double of 13."}, {'question': 'What is 41 + 41?', 'options': ['81', '82', '83', '84'], 'answer': 1, 'hint': "It's double of 41."}, {'question': 'What is 23 + 23?', 'options': ['45', '46', '47', '48'], 'answer': 1, 'hint': "It's double of 23."}, {'question': 'What is 39 + 39?', 'options': ['77', '78', '79', '80'], 'answer': 1, 'hint': "It's double of 39."}, {'question': 'What is 21 + 21?', 'options': ['41', '42', '43', '44'], 'answer': 1, 'hint': "It's double of 21."}, {'question': 'What is 32 + 32?', 'options': ['63', '64', '65', '66'], 'answer': 1, 'hint': "It's double of 32."}, {'question': 'What is 7 + 7?', 'options': ['13', '14', '15', '16'], 'answer': 1, 'hint': "It's double of 7."}, {'question': 'What is 17 + 17?', 'options': ['33', '34', '35', '36'], 'answer': 1, 'hint': "It's double of 17."}, {'question': 'What is 16 + 16?', 'options': ['31', '32', '33', '34'], 'answer': 1, 'hint': "It's double of 16."}, {'question': 'What is 8 + 8?', 'options': ['15', '16', '17', '18'], 'answer': 1, 'hint': "It's double of 8."}, {'question': 'What is 38 + 38?', 'options': ['75', '76', '77', '78'], 'answer': 1, 'hint': "It's double of 38."}, {'question': 'What is 30 + 30?', 'options': ['59', '60', '61', '62'], 'answer': 1, 'hint': "It's double of 30."}, {'question': 'What is 12 + 12?', 'options': ['23', '24', '25', '26'], 'answer': 1, 'hint': "It's double of 12."}, {'question': 'What is 45 + 45?', 'options': ['89', '90', '91', '92'], 'answer': 1, 'hint': "It's double of 45."}, {'question': 'What is 48 + 48?', 'options': ['95', '96', '97', '98'], 'answer': 1, 'hint': "It's double of 48."}, {'question': 'What is 46 + 46?', 'options': ['91', '92', '93', '94'], 'answer': 1, 'hint': "It's double of 46."}, {'question': 'What is 14 + 14?', 'options': ['27', '28', '29', '30'], 'answer': 1, 'hint': "It's double of 14."}, {'question': 'What is 26 + 26?', 'options': ['51', '52', '53', '54'], 'answer': 1, 'hint': "It's double of 26."}, {'question': 'What is 40 + 40?', 'options': ['79', '80', '81', '82'], 'answer': 1, 'hint': "It's double of 40."}, {'question': 'What is 33 + 33?', 'options': ['65', '66', '67', '68'], 'answer': 1, 'hint': "It's double of 33."}, {'question': 'What is 37 + 37?', 'options': ['73', '74', '75', '76'], 'answer': 1, 'hint': "It's double of 37."}, {'question': 'What is 44 + 44?', 'options': ['87', '88', '89', '90'], 'answer': 1, 'hint': "It's double of 44."}, {'question': 'What is 2 + 2?', 'options': ['3', '4', '5', '6'], 'answer': 1, 'hint': "It's double of 2."}, {'question': 'What is 10 + 10?', 'options': ['19', '20', '21', '22'], 'answer': 1, 'hint': "It's double of 10."}, {'question': 'What is 19 + 19?', 'options': ['37', '38', '39', '40'], 'answer': 1, 'hint': "It's double of 19."}, {'question': 'What is 6 + 6?', 'options': ['11', '12', '13', '14'], 'answer': 1, 'hint': "It's double of 6."}]

score = 0
hints_left = 3

print("🎮 Welcome to the Quiz Game!")
print("============================\n")

for idx, q in enumerate(questions):
    print(f"Q{idx + 1}: {q['question']}")
    for i, opt in enumerate(q['options']):
        print(f"   {i+1}. {opt}")

    use_hint = input("Do you want a hint? (yes/no): ").strip().lower()
    if use_hint == "yes" and hints_left > 0:
        print(f"Hint: {q['hint']}")
        hints_left -= 1
        print(f"Hints left: {hints_left}")
    elif use_hint == "yes":
        print("❌ No hints left.")

    try:
        ans = int(input("Enter your answer (1-4): ").strip()) - 1
        if ans == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['options'][q['answer']]}\n")
    except ValueError:
        print("❌ Invalid input. Moving to next question.\n")

print(f"🏁 Game Over! Your score: {score}/{len(questions)}")
