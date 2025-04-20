import nltk
from nltk.stem import WordNetLemmatizer
import random

lemmatizer = WordNetLemmatizer()

#DEFINING CHATBOX INTENTS
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "goodbye", "take care"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "much appreciated"],
        "responses": ["You're welcome!", "No problem!", "Anytime!"]
    },
    "about": {
        "patterns": ["who are you", "what is your name", "tell me about yourself"],
        "responses": ["I'm a chatbot built with Python and NLTK!", "I'm your friendly Python chatbot."]
    },
    "unknown": {
        "responses": ["Sorry, I don't understand.", "Could you please rephrase that?", "Hmm, not sure about that."]
    }
}

#PREPROCESSING USER INPUT
def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    lemmas = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmas

#MATCHING INTENTS
def match_intent(user_input):
    processed_input = preprocess(user_input)
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            pattern_words = preprocess(pattern)
            if set(pattern_words).intersection(processed_input):
                return intent
    return "unknown"

def chatbot():
    print("🤖 Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("🤖 Chatbot: Goodbye!")
            break
        intent = match_intent(user_input)
        response = random.choice(intents[intent]["responses"])
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    chatbot()
