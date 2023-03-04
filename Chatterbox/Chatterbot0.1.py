
from chatterbot import ChatBot as cb
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = cb('RubberDucky')
chatbot.storage.drop()
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")
''''
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Who Are you",
    "I'm a Rubber Ducky!,I can help you sove problems but taling to me.",
])
'''
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")