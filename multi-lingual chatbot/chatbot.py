import absl.logging
import google.generativeai as genai
from googletrans import Translator
import streamlit as st

# Suppress the verbosity of absl logging
absl.logging.set_verbosity(-1)

# Replace with your actual Gemini API key
api_key = "AIzaSyAU9XYaYmaDFGK5G2SjrMtecO-XFw6jGHA"

# Configure the Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# List of Indian languages and their corresponding ISO codes
indian_languages = {
    "Hindi": "hi",
    "English": "en",
    "Telugu": "te",
    "Tamil": "ta",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Odia": "or",
    "Bengali": "bn",
    "Assamese": "as",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Kashmiri": "ks",
    "Sindhi": "sd",
    "Sanskrit": "sa",
    "Konkani": "gom",
    "Manipuri": "mni",
    "Bodo": "brx",
    "Dogri": "dgr",
    "Maithili": "mai",
    "Santali": "sa",
    "Nepali": "ne",
    "Bhojpuri": "bho",
    "Magadhi": "mag",
}

# Initialize the Google Translator
translator = Translator()

def translate_chatbot_response(prompt, target_language):
    
    
    # Generate response using the Gemini model
    response = model.generate_content(prompt).text
    
    # Translate the response using Google Translate
    translated_text = translator.translate(response, dest=target_language).text
    
    return translated_text


st.title("Chatbot Translator")


prompt = st.text_input("Enter your query:")


target_language = st.selectbox("Select target language:", list(indian_languages.keys()))

if st.button("Submit"):
    if prompt and target_language:
       
        translated_response = translate_chatbot_response(prompt, indian_languages[target_language])
        st.write(f"Translated Response: {translated_response}")
    else:
        st.error("Please enter a query and select a language.")
        