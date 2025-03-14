import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("C:\\Users\\ASUS\\Desktop\\Implementation of ChatBot using NLP\\intents.json"))
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())  # Tokenization & Lowercasing
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in string.punctuation]
    return ' '.join(tokens)

# Load intents from the JSON file
file_path = os.path.abspath(r"C:\Users\ASUS\Desktop\Implementation of ChatBot using NLP\intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = RandomForestClassifier(n_estimators=200, random_state=42)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(preprocess_text(pattern))

# Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x.toarray(), y)  # Convert sparse matrix to dense format for RandomForest

def chatbot(input_text):
    input_text = preprocess_text(input_text)
    input_vector = vectorizer.transform([input_text]).toarray()
    tag = clf.predict(input_vector)[0]
    
    if "time" in input_text or "date" in input_text or "day" in input_text:
        now = datetime.datetime.now()
        if "time" in input_text:
            return f"The current time is {now.strftime('%H:%M:%S')}"
        elif "date" in input_text:
            return f"Today's date is {now.strftime('%Y-%m-%d')}"
        elif "day" in input_text:
            return f"Today is {now.strftime('%A')}"
    
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    
    return "I'm not sure I understand. Can you rephrase that?"

# Streamlit UI Enhancements
st.set_page_config(page_title="Chatbot", page_icon="💬", layout="wide")

# Sidebar Menu 
menu = ["Home", "Conversation History", "About"]
choice = st.sidebar.selectbox("Menu", menu)

st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center;'>Developed by: Amaan Haque</p>", unsafe_allow_html=True)

# Store conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if choice == "Home":
    st.title("🤖 Implementation of Chatbot using NLP")
    st.write("Ask me anything! Type below and press Enter.")
    
    # Chat input
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
    	# Append only if it's a new message
    	if "last_input" not in st.session_state or st.session_state.last_input != user_input:
            st.session_state.last_input = user_input  # Store last input to prevent duplicate processing
        
            # Store user message
            st.session_state.chat_history.append({"role": "user", "message": user_input})
        
            # Generate response
            with st.spinner("Thinking..."):
               response = chatbot(user_input)
        
            # Store chatbot response
            st.session_state.chat_history.append({"role": "bot", "message": response})
        
            # Save to CSV
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, response, timestamp])
    
    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message("user" if chat["role"] == "user" else "assistant"):
            st.write(chat["message"])
    
elif choice == "Conversation History":
    st.header("📜 Conversation History")
    try:
        with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                st.text(f"User: {row[0]}")
                st.text(f"Chatbot: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")
    except FileNotFoundError:
        st.write("No conversation history found.")
    
elif choice == "About":
    st.header("ℹ️ About")
    st.write("The goal of this project is to create a chatbot that can understand and respond to user input based on intents. The chatbot is built using Natural Language Processing (NLP) and RandomForestClassifier for better accuracy. The chatbot is built using Streamlit, a Python library for building interactive web applications.")
    
    st.subheader("Project Overview:")
    st.write("""
    The project is divided into two parts:
    1. NLP techniques and RandomForestClassifier algorithm is used to train the chatbot on labeled intents and entities.
    2. For building the Chatbot interface, Streamlit web framework is used to build a web-based chatbot interface. The interface allows users to input text and receive responses from the chatbot.
    """)
    
    st.subheader("Dataset:")
    st.write("""
    The dataset used in this project is a collection of labelled intents and entities. The data is stored in a list.
    - Intents: The intent of the user input (e.g. "greeting", "budget", "about")
    - Entities: The entities extracted from user input (e.g. "Hi", "How do I create a budget?", "What is your purpose?")
    - Text: The user input text.
    """)
    
    st.subheader("Streamlit Chatbot Interface:")
    st.write("The chatbot interface is built using Streamlit. The interface includes a text input box for users to input their text and a chat window to display the chatbot's responses. The interface uses the trained model to generate responses to user input.")
    
    st.subheader("Conclusion:")
    st.write("In this project, a chatbot is built that can understand and respond to user input based on intents. The chatbot was trained using NLP and RandomForestClassifier, and the interface was built using Streamlit. This project can be extended by adding more data, using more sophisticated NLP techniques, deep learning algorithms.")
