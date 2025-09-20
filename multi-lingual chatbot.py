import absl.logging
import google.generativeai as genai
from googletrans import Translator, LANGUAGES
import streamlit as st
import os
import datetime
import json


def translate_chatbot_response(prompt, target_language_code):
    response = model.generate_content(prompt).text
    
    # Check if Google Translate supports this code
    if target_language_code not in LANGUAGES:
        translated_text = f"(Translation not available for {target_language_code})"
    else:
        translated_text = translator.translate(response, dest=target_language_code).text
    
    return response, translated_text


# Suppress absl logging
absl.logging.set_verbosity(-1)

# Configure Gemini API
api_key = "ADD_YOUR_API"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Indian languages
indian_languages = {
    "Hindi": "hi",
    "English": "en",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Odia": "or"
}

translator = Translator()

# History folder
HISTORY_DIR = "history"
os.makedirs(HISTORY_DIR, exist_ok=True)

def translate_chatbot_response(prompt, target_language):
    response = model.generate_content(prompt).text
    translated_text = translator.translate(response, dest=target_language).text
    return response, translated_text

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

# --- Sidebar with history ---
st.sidebar.title("📜 Chat History")

# New Chat button
if st.sidebar.button("➕ New Chat"):
    st.session_state.current_chat = None  # Clear current chat
    st.session_state.new_prompt = ""      # Clear input box for new chat

if st.session_state.chat_history:
    for i, chat in enumerate(reversed(st.session_state.chat_history)):
        label = f"{chat['time']} - {chat['query'][:25]}..."
        if st.sidebar.button(label, key=f"chat_{i}"):
            # Load that chat back into current_chat (including language)
            st.session_state.current_chat = chat
else:
    st.sidebar.info("No past chats yet!")

# --- Main UI ---
st.markdown("<h1 style='text-align: center; color: cyan;'>🤖 Chatbot Translator</h1>", unsafe_allow_html=True)

# Pre-fill input box if editing existing chat
prompt = st.text_input(
    "✍️ Enter your query:",
    value=st.session_state.current_chat['query'] if st.session_state.current_chat else "",
    key="new_prompt"
)

target_language = st.selectbox(
    "🌐 Select target language:",
    list(indian_languages.keys()),
    index=list(indian_languages.keys()).index(st.session_state.current_chat['language']) if st.session_state.current_chat else 0
)

if st.button("Submit"):
    if prompt and target_language:
        response, translated_response = translate_chatbot_response(prompt, indian_languages[target_language])

        if st.session_state.current_chat:
            # Update existing chat in history if it exists
            for idx, chat in enumerate(st.session_state.chat_history):
                if chat["time"] == st.session_state.current_chat["time"]:
                    st.session_state.chat_history[idx].update({
                        "query": prompt,
                        "response": response,
                        "translated": translated_response,
                        "language": target_language
                    })
                    break
            st.session_state.current_chat.update({
                "query": prompt,
                "response": response,
                "translated": translated_response,
                "language": target_language
            })
        else:
            # Create a new chat and add it to history
            new_chat = {
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "query": prompt,
                "response": response,
                "translated": translated_response,
                "language": target_language
            }
            st.session_state.chat_history.append(new_chat)
            st.session_state.current_chat = new_chat

        # Save history to disk
        filename = os.path.join(
            HISTORY_DIR,
            f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(st.session_state.chat_history, f, ensure_ascii=False, indent=4)

# --- Show current chat ---
if st.session_state.current_chat:
    chat = st.session_state.current_chat
    st.markdown(
        f"""
        <div style="background-color:#1E1E1E; padding:12px; border-radius:10px; margin-top:20px; border-left:5px solid cyan;">
        <p><b>🕒 {chat['time']}</b></p>
        <p><b>📝 You:</b> {chat['query']}</p>
        <p><b>🤖 Bot:</b> <span style='color:lightgreen;'>{chat['response']}</span></p>
        <p><b>🌐 Translated ({chat['language']}):</b> <span style='color:orange;'>{chat['translated']}</span></p>
        </div>
        """,
        unsafe_allow_html=True
    )
