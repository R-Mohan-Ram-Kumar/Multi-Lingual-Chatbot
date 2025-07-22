🤖 Multilingual Chatbot Translator using Gemini API and Streamlit
This project is a multilingual chatbot web application built using Google's Gemini API, Streamlit, and Google Translate. It allows users to input queries in English and receive responses from the chatbot, translated into one of several Indian regional languages.

🔧 Features
🧠 Uses Gemini 1.5 Flash to generate intelligent responses

🌐 Translates chatbot responses into 25+ Indian languages

🖥️ Built using Streamlit for a fast and interactive web interface

🔁 Real-time translation using Google Translate API

📉 Suppresses unnecessary logging for clean performance


🚀 Demo
Launch the app by running:

streamlit run app.py



🧰 Tech Stack
💬 Google Gemini API (1.5 Flash)

🌐 Streamlit

🌍 Googletrans

🐍 Python 3.8+

📦 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/multilingual-chatbot.git
cd multilingual-chatbot
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your Gemini API key

Replace the line in app.py:

python
Copy
Edit
api_key = "Enter_YOUR_GEMINI_API_KEY"
with your actual key:

python
Copy
Edit
api_key = "your_real_api_key"
Run the Streamlit app

streamlit run app.py


📁 File Structure

multilingual-chatbot/
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


Input	Translated Output
"What is AI?"	"ఏఐ అంటే ఏమిటి?" (Telugu)
"How does Machine Learning work?"	"मशीन लर्निंग कैसे काम करता है?" (Hindi)

✍️ Author
Mohan Ram Kumar

🔗 https://www.linkedin.com/in/mohan-ram-kumar-35799b268/
🐙 https://github.com/R-Mohan-Ram-Kumar


🌟 Contribute
Feel free to fork the repository, open issues, or submit PRs to improve this project!
