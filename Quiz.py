import streamlit as st
import random

st.set_page_config(page_title="Nepali Quiz Game", page_icon="🧠", layout="centered")

# ---------------------- Styling ----------------------
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
    </style>
""", unsafe_allow_html=True)

# ---------------------- Question Bank ----------------------
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
] * 5  # replicate to make 50

random.shuffle(questions)

# ---------------------- Session State ----------------------
if "page" not in st.session_state:
    st.session_state.page = "login"
if "score" not in st.session_state:
    st.session_state.score = 0
if "user" not in st.session_state:
    st.session_state.user = None
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

# ---------------------- Functions ----------------------
def login(username, password):
    if username and password:
        st.session_state.user = username
        st.session_state.page = "quiz"

def register(username, password):
    if username and password:
        st.session_state.user = username
        st.session_state.page = "quiz"

def next_question():
    st.session_state.question_index += 1
    if st.session_state.question_index >= len(questions):
        st.session_state.page = "leaderboard"

def reset_game():
    st.session_state.page = "login"
    st.session_state.score = 0
    st.session_state.question_index = 0

# ---------------------- Login Page ----------------------
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

# ---------------------- Quiz Page ----------------------
elif st.session_state.page == "quiz":
    q = questions[st.session_state.question_index]
    st.markdown(f"<div class='question'>{q['question']}</div>", unsafe_allow_html=True)

    for option in q["options"]:
        if st.button(option, use_container_width=True):
            if option == q["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! Correct: {q['answer']}")
            st.button("Next", on_click=next_question)

    st.info(f"Question {st.session_state.question_index + 1} / {len(questions)}")
    st.info(f"Score: {st.session_state.score}")

# ---------------------- Leaderboard Page ----------------------
elif st.session_state.page == "leaderboard":
    st.title("🏆 Quiz Complete!")
    st.success(f"{st.session_state.user}, you scored {st.session_state.score} / {len(questions)}")

    st.session_state.leaderboard.append((st.session_state.user, st.session_state.score))
    sorted_leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x[1], reverse=True)

    st.subheader("Leaderboard")
    for i, (user, score) in enumerate(sorted_leaderboard[:10]):
        st.write(f"{i+1}. {user} — {score}")

    if st.button("Play Again"):
        reset_game()
