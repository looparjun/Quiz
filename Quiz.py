# app.py

import streamlit as st
import random

# 50 sample questions
questions = [
    {"question": "What is 2 + 2?", "options": ["1", "2", "3", "4"], "answer": "4"},
    {"question": "Capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What color is the sky?", "options": ["Blue", "Green", "Red", "Yellow"], "answer": "Blue"},
    # Add more questions here...
] * 17  # Repeat to simulate 50 questions (adjust as needed)
random.shuffle(questions)

st.title("🎯 Streamlit Quiz Game")

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0

# Load current question
q = questions[st.session_state.index]

st.markdown(f"**Q{st.session_state.index + 1}: {q['question']}**")
user_choice = st.radio("Choose one:", q["options"])

if st.button("Submit"):
    if user_choice == q["answer"]:
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Wrong! Correct answer was: {q['answer']}")
    
    st.session_state.index += 1

    if st.session_state.index >= len(questions):
        st.balloons()
        st.write(f"🎉 Quiz Finished! Your score: {st.session_state.score}/{len(questions)}")
        if st.button("Restart"):
            st.session_state.index = 0
            st.session_state.score = 0
else:
    st.write("👆 Select your answer and click Submit!")

