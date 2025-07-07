import streamlit as st
from textblob import TextBlob
import datetime

# --- App Config ---
st.set_page_config(page_title="MoodSense", page_icon="😊", layout="centered")

# --- Title ---
st.title("🌟 MoodSense: AI-Powered Emoji Mood Detector")
st.markdown("Enter your text below, and let AI detect your current emotion!")

# --- User Input ---
user_input = st.text_area("💬 Type your message here:")

# --- Function to detect mood ---
def get_emoji_and_mood(sentiment):
    if sentiment > 0.1:
        return "😄", "Happy"
    elif sentiment < -0.1:
        return "😢", "Sad"
    else:
        return "😐", "Neutral"

# --- Main Logic ---
if user_input:
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    emoji, mood = get_emoji_and_mood(sentiment)

    st.markdown("### 🧠 Mood Analysis Result")
    st.write(f"**Mood:** {mood}")
    st.write(f"**Emoji:** {emoji}")
    st.write(f"**Sentiment Score:** {sentiment:.2f}")
    st.caption(f"Analyzed on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
