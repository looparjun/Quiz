import streamlit as st
import random
import time
from threading import Timer

st.set_page_config(page_title="Nepali Quiz Game", page_icon="🧠", layout="centered")

# -------- Styling --------
st.markdown("""
<style>
.title { text-align: center; font-size: 2.5em; color: #00FFAA; }
.subtitle { text-align: center; font-size: 1.3em; color: #FFDD00; margin-bottom: 30px; }
.question { font-size: 1.3em; font-weight: bold; }
.option-btn {
    background-color: #333;
    padding: 10px 20px;
    border-radius: 8px;
    color: white;
    text-align: center;
    margin: 5px;
    cursor: pointer;
    transition: all 0.3s;
}
.option-btn:hover {
    background-color: #555;
}
.timer {
    font-weight: bold;
    font-size: 1.5em;
    color: #FF5555;
    text-align: center;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------- Question Bank --------
questions = [
    {"question": "What is the capital of Nepal?", "options": ["Pokhara", "Lalitpur", "Kathmandu", "Biratnagar"], "answer": "Kathmandu"},
    {"question": "What is 12 x 8?", "options": ["96", "108", "84", "88"], "answer": "96"},
    {"question": "Who discovered gravity?", "options": ["Einstein", "Newton", "Galileo", "Tesla"], "answer": "Newton"},
    {"question": "Which is the largest planet?", "options": ["Earth", "Mars", "Saturn", "Jupiter"], "answer": "Jupiter"},
    {"question": "नेपालको राष्ट्रिय जनावर के हो?", "options": ["गाई", "कुकुर", "बाघ", "भालु"], "answer": "गाई"},
    {"question": "The Great Wall is located in?", "options": ["Japan", "India", "China", "Thailand"], "answer": "China"},
    {"question": "Kathmandu lies in which valley?", "options": ["Pokhara", "Terai", "Bagmati", "Kathmandu"], "answer": "Kathmandu"},
    {"question": "5 + 9 * 2 = ?", "options": ["28", "23", "18", "17"], "answer": "23"},
    {"question": "Who is known as the Light of Asia?", "options": ["Ashoka", "Buddha", "Gandhi", "Lincoln"], "answer": "Buddha"},
    {"question": "Which gas do plants need?", "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
] * 5  # 50 questions

random.shuffle(questions)

# -------- Session State Setup --------
if "page" not in st.session_state:
    st.session_state.page = "login"
if "score" not in st.session_state:
    st.session_state.score = 0
if "user" not in st.session_state:
    st.session_state.user = None
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "leaderboard" not in st.session_state:
    # Dict: username -> highest score
    st.session_state.leaderboard = {}
if "timer_start" not in st.session_state:
    st.session_state.timer_start = None
if "time_up" not in st.session_state:
    st.session_state.time_up = False
if "answered" not in st.session_state:
    st.session_state.answered = False

# -------- Timer Functions --------
def start_timer():
    st.session_state.timer_start = time.time()
    st.session_state.time_up = False
    st.session_state.answered = False

def check_timer():
    if st.session_state.timer_start:
        elapsed = time.time() - st.session_state.timer_start
        remaining = 3 - elapsed
        if remaining <= 0:
            st.session_state.time_up = True
            if not st.session_state.answered:
                st.session_state.score = 0
            return 0
        return remaining
    return 3

def next_question():
    st.session_state.question_index += 1
    if st.session_state.question_index >= len(questions):
        st.session_state.page = "leaderboard"
    else:
        start_timer()
        st.experimental_rerun()

def reset_game():
    st.session_state.page = "login"
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.user = None
    st.session_state.timer_start = None
    st.session_state.time_up = False
    st.session_state.answered = False

# -------- Login and Register --------
def login(username, password):
    if username and password:
        st.session_state.user = username
        st.session_state.page = "quiz"
        start_timer()

def register(username, password):
    if username and password:
        # Just register as login for demo
        st.session_state.user = username
        st.session_state.page = "quiz"
        start_timer()

# -------- Main App --------
if st.session_state.page == "login":
    st.markdown("<div class='title'>🧠 Nepali Quiz Game</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Login or Register to Begin</div>", unsafe_allow_html=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            login(username, password)
    with col2:
        if st.button("Register"):
            register(username, password)

elif st.session_state.page == "quiz":
    # Show question & timer
    q = questions[st.session_state.question_index]
    st.markdown(f"<div class='question'>{q['question']}</div>", unsafe_allow_html=True)
    
    remaining = check_timer()
    st.markdown(f"<div class='timer'>⏰ Time left: {remaining:.1f} seconds</div>", unsafe_allow_html=True)

    if st.session_state.time_up:
        st.error("⏳ Time's up! Score reset to 0.")
        st.session_state.score = 0
        st.session_state.time_up = False
        st.button("Next Question", on_click=next_question)
    else:
        # Disable options if answered or time's up
        disabled = st.session_state.answered or st.session_state.time_up
        
        for option in q["options"]:
            if st.button(option, disabled=disabled, use_container_width=True):
                st.session_state.answered = True
                if option == q["answer"]:
                    st.success("✅ Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Wrong! Correct answer: {q['answer']}")
                    st.session_state.score = 0
                # Update leaderboard on every answered question
                current_score = st.session_state.leaderboard.get(st.session_state.user, 0)
                if st.session_state.score > current_score:
                    st.session_state.leaderboard[st.session_state.user] = st.session_state.score
                st.button("Next Question", on_click=next_question)

    st.info(f"Question {st.session_state.question_index + 1} / {len(questions)}")
    st.info(f"Current Score: {st.session_state.score}")

elif st.session_state.page == "leaderboard":
    st.title("🏆 Quiz Complete!")
    st.success(f"{st.session_state.user}, your final score is {st.session_state.score} / {len(questions)}")
    
    # Add/update leaderboard record
    current_score = st.session_state.leaderboard.get(st.session_state.user, 0)
    if st.session_state.score > current_score:
        st.session_state.leaderboard[st.session_state.user] = st.session_state.score

    st.subheader("Real-Time Leaderboard (Top Scores)")
    sorted_leaderboard = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)
    for i, (user, score) in enumerate(sorted_leaderboard[:10]):
        st.write(f"{i+1}. {user} — {score}")

    # Auto refresh leaderboard every 2 seconds (without user refresh)
    time.sleep(2)
    st.experimental_rerun()

    if st.button("Play Again"):
        reset_game()
