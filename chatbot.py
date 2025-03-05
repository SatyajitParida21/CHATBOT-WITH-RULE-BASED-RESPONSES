import re

def chatbot_response(user_input):
    responses = {
        r'hi|hello|hey': [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! Need any help?"
        ],
        r'how are you': [
            "I'm just a bot, but I'm  functioning perfectly! How about you?",
            "I'm here and ready to assist! What’s on your mind?"
        ],
        r'what is your name|who are you': [
            "I am a chatbot created to assist you! You can call me ChatBot.",
            "I'm your virtual assistant. How can I help you today?"
        ],
        r'bye|goodbye|see you': [
            "Goodbye! Have a great day!",
            "See you later! Feel free to return if you need more help.",
            "Bye! Take care!"
        ],
      
        r'what can you do': [
            "I can answer your questions, chat  with you, and assist in various tasks. Give it a try!",
            "I'm here to provide information, chat, and help you with general queries."
        ],

        r'thank you|thanks': [
            "You're welcome! Happy to help!",
            "No problem! Let me know if you need anything else."
        ],
        r'how does AI work': [
            "AI works by processing data, learningfrom patterns, and making decisions  based on algorithmsand models.",
            "Artificial Intelligence mimics human intelligence using algorithms and large datasets."
        ],

        r'what is machine learning': [
            "Machine learning is a subset of AI that enables computers to learn from data and improve their  performance without being explicitly programmed.",
            "Machine learning uses algorithms to identify patterns in data and make predictions or decisions."
        ],
        r'what is the capital of (.+)': [
            "I'm not sure, but  you can check  on Google!",
            "You might want  to look that  up online!"
        ],
        r'how old are you': [
            "I'm just a digital being, so  I don't age! But  I'm always learning new things!",
            "I don't have  an age, but I’m always up to date  with the latest knowledge!"
        ],


        r'tell me a joke': [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
   
        r'what is python': [
            "Python is a popular programming language known for its simplicity and versatility.",
            "Python is a powerful programming language used in web development, data science, AI, and more."
        ]
    }
    
    user_input = user_input.lower()
    for pattern, response_list in responses.items():
        if re.search(pattern, user_input):
            return response_list[0]  # Return the first response found
    
    return "I'm sorry, I don't understand that. Can you rephrase?"

# Chat loop
print("ChatBot: Hello! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye! Have a great day!")
        break
    print("ChatBot:", chatbot_response(user_input))
