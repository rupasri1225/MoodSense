import streamlit as st
from textblob import TextBlob
import datetime

# --- Page Config ---
st.set_page_config(page_title="MoodSense 😊", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        html, body {
            background-color: #f3f4f8;
            font-family: 'Segoe UI', sans-serif;
        }

        .main-container {
            background-color: #ffffff;
            margin-top: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            max-width: 100%;
        }

        .stTextInput input {
            background-color: #fffdf7;
            border-radius: 10px;
            padding: 0.75rem;
            font-size: 16px;
            color: #333;
        }

        .stButton button {
            background-color: #0a8754;
            color: white;
            font-weight: bold;
            font-size: 16px;
            border-radius: 10px;
            padding: 0.75rem 1.5rem;
            width: 100%;
            transition: 0.3s ease-in-out;
        }

        .stButton button:hover {
            background-color: #0c9c61;
        }

        .emoji-output {
            font-size: 48px;
            text-align: center;
            margin-top: 1rem;
        }

        .footer {
            text-align: center;
            font-size: 14px;
            color: gray;
            margin-top: 2rem;
        }

        @media (max-width: 768px) {
            .main-container {
                padding: 1rem;
            }
            .stTextInput input {
                font-size: 15px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- Layout Container ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- Title & Description ---
st.markdown("<h1 style='text-align: center;'>😊 MoodSense</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #0a8754;'>AI-Powered Emoji Mood Detector</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analyze your emotion based on what you type!</p>", unsafe_allow_html=True)

# --- User Input ---
user_input = st.text_input("✏️ Enter your message:")

# --- Mood Detection Function ---
def get_emoji_and_mood(sentiment):
    if sentiment > 0.1:
        return "😄", "Happy"
    elif sentiment < -0.1:
        return "😢", "Sad"
    else:
        return "😐", "Neutral"

# --- Output Section ---
if user_input:
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    emoji, mood = get_emoji_and_mood(sentiment)

    st.markdown("### 🧠 Mood Analysis Result")
    st.markdown(f"<div class='emoji-output'>{emoji}</div>", unsafe_allow_html=True)
    st.success(f"**Mood:** {mood}")
    st.info(f"**Sentiment Score:** {sentiment:.2f}")
    st.caption(f"Analyzed on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# --- Footer Branding ---
st.markdown("</div>", unsafe_allow_html=True)
st.markdown('<div class="footer">Designed with 💚 by <b>Yarramsetti Rupa Sri</b></div>', unsafe_allow_html=True)
