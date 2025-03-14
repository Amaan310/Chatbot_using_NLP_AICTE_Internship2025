**🤖 Implementation of Chatbot using NLP** (🚀 AICTE Internship_2025 in partnership with Edunet & Shell on Artificial Intelligence with Green Technology 🌱🤖)
🔹 A smart AI-powered chatbot built using Natural Language Processing (NLP) and Machine Learning to understand and respond to user queries.

**📌 Table of Contents**
📜 About the Project
🛠️ Features
⚙️ Technologies Used
📂 Project Structure
🚀 Installation & Setup
📸 Screenshots
📌 Future Enhancements
🤝 Contributing
📞 Contact

**📜 About the Project**
This chatbot is designed to understand and classify user queries using Natural Language Processing (NLP) techniques. It employs RandomForestClassifier for intent classification and is deployed using Streamlit for an interactive UI.

**✨ Key Objectives:**
✅ Improve chatbot understanding using advanced text preprocessing.
✅ Achieve high response accuracy with RandomForestClassifier.
✅ Provide a user-friendly interface via Streamlit.
✅ Implement real-time time, date, and day retrieval.

**🛠️ Features:**
🚀 Smart Intent Recognition - Accurately classifies user queries.
📊 Machine Learning-Based Responses - Uses RandomForestClassifier for high accuracy.
🔠 NLP Preprocessing - Includes lemmatization, stopword removal, and tokenization.
🎨 Streamlit UI - Provides an interactive web-based chatbot interface.
🕒 Dynamic Information Retrieval - Can fetch time, date, and day when asked.
📁 Conversation Logging - Stores chat history for future analysis.

**⚙️ Technologies Used-**
🔹 Programming Language: Python 🐍
🔹 Machine Learning Model: RandomForestClassifier 🌲
🔹 Libraries Used:
    NLTK – For text preprocessing (Tokenization, Stopword Removal, Lemmatization)
    Scikit-learn – For ML model training
    Streamlit – For building the chatbot UI
    JSON – For storing chatbot intents and responses

**📂 Project Structure:**

📂 Chatbot-NLP-Project/
│── 📜 README.md              <- Project Documentation  
│── 📂 chatbot.py             <- Main chatbot script  
│── 📂 intents.json           <- Dataset containing chatbot intents & responses  
│── 📂 requirements.txt       <- Dependencies for running the chatbot  
│── 📂 chat_log.csv           <- Conversation history (auto-generated)  
│── 📂 assets/                <- Screenshots & visuals  
│── 📂 templates/             <- Streamlit UI components  

**🚀 Installation & Setup**
To run this project on your local system, follow these steps:

1️⃣ Clone the Repository-
git clone https://github.com/your-username/Chatbot-NLP-Project.git
cd Chatbot-NLP-Project

2️⃣ Install Dependencies-
pip install -r requirements.txt

3️⃣ Run the Chatbot-
streamlit run chatbot.py

**📌 Future Enhancements:**
🚀 Deep Learning Model – Upgrade to a Transformer-based model (BERT) for better accuracy.
🔍 Context-Awareness – Improve chatbot memory for better multi-turn conversations.
📡 API Integration – Connect chatbot with external services (e.g., Google Calendar, Weather API).

**🤝 Contributing:**
🔹 Want to contribute? Fork this repository and submit a pull request!
