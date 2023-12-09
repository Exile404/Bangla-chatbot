from googletrans import Translator

def translate_text(text, target_language='bn'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def translate_list(list_to_translate):
    translated_list = []

    for item in list_to_translate:
        translated_item = {
            'tag': item['tag'],
            'patterns': [translate_text(pattern) for pattern in item['patterns']],
            'responses': [translate_text(response) for response in item['responses']]
        }
        print('OK')
        translated_list.append(translated_item)

    return translated_list


original_list = [
  {
    "tag": "greeting",
    "patterns": [
      "Hi",
      "Hey",
      "How are you",
      "Is anyone there?",
      "Hello",
      "Good day"
    ],
    "responses": [
      "Hey :-)",
      "Hello, thanks for visiting",
      "Hi there, what can I do for you?",
      "Hi there, how can I help?"
    ]
  },
  {
    "tag": "farewell",
    "patterns": [
      "Goodbye",
      "See you later",
      "Farewell",
      "Bye",
      "Take care"
    ],
    "responses": [
      "Goodbye! Have a great day.",
      "See you later!",
      "Farewell, come back soon.",
      "Bye! Take care."
    ]
  },
  {
    "tag": "thanks",
    "patterns": [
      "Thank you",
      "Thanks a lot",
      "Appreciate it",
      "Thanks for your help"
    ],
    "responses": [
      "You're welcome!",
      "Glad I could help.",
      "No problem, happy to assist.",
      "Anytime! Let me know if you need more help."
    ]
  },
  {
    "tag": "about_bot",
    "patterns": [
      "What are you?",
      "Who are you?",
      "Tell me about yourself"
    ],
    "responses": [
      "I am a chatbot designed to assist you.",
      "I'm a virtual assistant here to help you.",
      "I'm a chatbot created to answer your questions and provide assistance."
    ]
  },
  {
    "tag": "help",
    "patterns": [
      "Help",
      "Can you help me?",
      "I need assistance"
    ],
    "responses": [
      "Of course! What do you need help with?",
      "I'm here to help. What can I do for you?",
      "Sure, I'll do my best to assist you. What's the issue?"
    ]
  },
  {
    "tag": "weather",
    "patterns": [
      "What's the weather like?",
      "Tell me about the weather",
      "Is it going to rain today?",
      "Weather forecast"
    ],
    "responses": [
      "I'm sorry, I don't have real-time weather information. You may check a weather website or app for the latest updates.",
      "Unfortunately, I can't provide current weather information. Please check a reliable weather source for accurate details."
    ]
  },
  {
    "tag": "jokes",
    "patterns": [
      "Tell me a joke",
      "Give me a funny joke",
      "Joke of the day"
    ],
    "responses": [
      "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!",
      "Here's a light-hearted one: Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
  },
  {
    "tag": "tech_support",
    "patterns": [
      "My computer is not working",
      "I have a technical issue",
      "Help with my device"
    ],
    "responses": [
      "I'm not a technical support expert, but I can try to offer some general advice. Have you tried turning it off and on again?",
      "For technical issues, it's best to contact your device's support or consult a professional technician for assistance."
    ]
  },
  {
    "tag": "movies",
    "patterns": [
      "Recommend a movie",
      "What's a good film to watch?",
      "Tell me about popular movies"
    ],
    "responses": [
      "Sure, I recommend checking out [Movie Title]. It has great reviews and an interesting plot!",
      "If you're into [genre], you might enjoy [Movie Title]. It's highly rated by audiences."
    ]
  },
  {
    "tag": "food",
    "patterns": [
      "What should I eat?",
      "Recommend a restaurant",
      "Tell me about your favorite food"
    ],
    "responses": [
      "It depends on your preferences! If you like [cuisine], you might enjoy [Restaurant Name].",
      "One of my favorite foods is [Your Favorite Dish]. It's delicious!"
    ]
  },
  {
    "tag": "music",
    "patterns": [
      "Recommend a song",
      "What's your favorite music?",
      "Tell me about popular artists"
    ],
    "responses": [
      "I recommend listening to [Song Title] by [Artist]. It's a great track!",
      "If you like [genre], you might enjoy the music of [Artist]."
    ]
  },
  {
    "tag": "travel",
    "patterns": [
      "Tell me about a great travel destination",
      "Recommend a vacation spot",
      "Travel tips"
    ],
    "responses": [
      "One amazing travel destination is [Location]. It offers breathtaking scenery and cultural experiences.",
      "For a relaxing vacation, consider visiting [Destination]. It's known for its beautiful beaches and vibrant culture."
    ]
  },
  {
    "tag": "education",
    "patterns": [
      "Tell me about online courses",
      "Recommend a book",
      "Study tips"
    ],
    "responses": [
      "There are many online platforms offering courses on various subjects. Consider checking out [Platform] for a wide range of courses.",
      "A highly recommended book is [Book Title] by [Author]. It's informative and engaging."
    ]
  }
]

translated_list = translate_list(original_list)

# Print the translated list
for item in translated_list:
    print(item)