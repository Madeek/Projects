import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [

    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you.', 'I\'m doing well, thanks for asking.']),
    (r'what\'?s your name?', ['You can call me Chatbot.', 'I am a chatbot.']),
    (r'(.*) your name(.*)', ['You can call me Chatbot.', 'I am a chatbot.']),
    (r'(.*) your age(.*)', ['I am ageless!', 'Age is just a number for me.']),
    (r'(.*) (good|well)', ['That\'s great to hear!', 'Awesome!']),
    (r'(.*) (bad|not good)', ['I\'m sorry to hear that.', 'Hope things get better.']),
    (r'(.*)', ['Interesting, tell me more.', 'I see.', 'Tell me more.'])
]

# Create a Chatbot
chatbot = Chat(patterns, reflections)

# Start conversation
print("Chatbot: Hello! I'm a simple chatbot. How can I assist you today?")

while True:

    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)

    if user_input.lower() == 'bye':
        
        break
