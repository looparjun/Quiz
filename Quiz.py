import streamlit as st
import random
import json
import os
import time
import threading

# ---- Local Leaderboard Storage ----
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return {}

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---- Sample Questions ----
QUESTIONS = [
    {"question": "What is the capital of Nepal?", "options": ["Pokhara", "Lalitpur", "Kathmandu", "Biratnagar"], "answer": "Kathmandu"},
    {"question": "What is 12 x 8?", "options": ["96", "108", "84", "88"], "answer": "96"},
    {"question": "Who discovered gravity?", "options": ["Einstein", "Newton", "Galileo", "Tesla"], "answer": "Newton"},
    {"question": "नेपालको राष्ट्रिय जनावर के हो?", "options": ["गाई", "कुकुर", "बाघ", "भालु"], "answer": "गाई"},
]

random.shuffle(QUESTIONS)

# ---- Session State ----
if "name" not in st.session_state:
    st.session_state.name = ""
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_idx" not in st.session_state:
    st.session_state.question_idx = 0
if "timer" not in st.session_state:
    st.session_state.timer = 5
if "answer_given" not in st.session_state:
    st.session_state.answer_given = False

# ---- Countdown ----
def countdown():
    while st.session_state.timer > 0 and not st.session_state.answer_given:
        time.sleep(1)
        st.session_state.timer -= 1
        st.experimental_rerun()

# ---- Login Screen ----
if not st.session_state.logged_in:
    st.title("🧠 Simple Quiz App")
    name = st.text_input("Enter your name to start:")
    if st.button("Start"):
        if name.strip():
            st.session_state.name = name.strip()
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.warning("Please enter a name.")

# ---- Quiz Game ----
else:
    q = QUESTIONS[st.session_state.question_idx]
    st.subheader(f"Question {st.session_state.question_idx + 1} of {len(QUESTIONS)}")
    st.write(q["question"])
    st.write(f"⏱️ Time left: {st.session_state.timer} seconds")

    if not st.session_state.answer_given:
        for option in q["options"]:
            if st.button(option):
                st.session_state.answer_given = True
                if option == q["answer"]:
                    st.success("✅ Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Wrong! Correct answer: {q['answer']}")
                    st.session_state.score = 0
                st.experimental_rerun()

        if st.session_state.timer == 5:
            threading.Thread(target=countdown, daemon=True).start()
    else:
        if st.button("Next"):
            st.session_state.answer_given = False
            st.session_state.timer = 5
            st.session_state.question_idx += 1

            if st.session_state.question_idx >= len(QUESTIONS):
                # Save score
                leaderboard = load_leaderboard()
                leaderboard[st.session_state.name] = max(
                    leaderboard.get(st.session_state.name, 0),
                    st.session_state.score
                )
                save_leaderboard(leaderboard)

                st.success("🎉 Quiz completed!")
                st.write(f"Final Score: {st.session_state.score}")
                if st.button("View Leaderboard"):
                    st.session_state.view_lb = True
                if st.button("Restart"):
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                st.stop()

            st.experimental_rerun()

    st.write(f"Your Score: {st.session_state.score}")

    st.markdown("---")
    st.subheader("🏆 Leaderboard")
    leaderboard = load_leaderboard()
    sorted_lb = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_lb[:10], 1):
        st.write(f"{i}. {name}: {score}")

    if st.button("Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
