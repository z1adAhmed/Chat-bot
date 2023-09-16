from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import time 
time.clock = time.time
import logging 
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)



# Create a new ChatBot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)



# Train the chatbot on English language data
for file in os.listdir('Data/'):
    data = open('Data/'+file, 'r', encoding='utf-8').readlines()
    trainer.train(data)


# Start a conversation with the chatbot
print("               WELCOME                ")
print(" press e to exit ")
while True:
    user_input = input("Ziad: ")
    if user_input.lower() == "e":
         exit()
    else:
        response = chatbot.get_response(user_input)
        print("Bot:", response)