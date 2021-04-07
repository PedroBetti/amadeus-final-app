'''
*****************************************************************************************************


███████╗████████╗██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██╗      █████╗ ██████╗ ███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██║     ██╔══██╗██╔══██╗██╔════╝
███████╗   ██║   ██████╔╝███████║   ██║   ██║   ██║███████╗    ██║     ███████║██████╔╝███████╗
╚════██║   ██║   ██╔══██╗██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██╔══██║██╔══██╗╚════██║
███████║   ██║   ██║  ██║██║  ██║   ██║   ╚██████╔╝███████║    ███████╗██║  ██║██████╔╝███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝


****************************************************************************************************

*** REDEFINING THE IMPOSSIBLE ***
*** 2020 - 2021 ***

*** Project id : AMADEUS ***
*** Description : Adaptive speech A.I. system using ML/NeuralNet/Tensorflow in Python/Java/HTML5 *** 
*** Researcher : Pedro H.C. Betti ***


****************************************************************************************************
'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

resp = "you"

# Creating ChatBot Instance
chatbot = ChatBot('Kona')


 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

#BANNER
print("")
print("")
print("  █████╗ ███╗   ███╗ █████╗ ██████╗ ███████╗██╗   ██╗███████╗")
print(" ██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝██║   ██║██╔════╝")
print(" ███████║██╔████╔██║███████║██║  ██║█████╗  ██║   ██║███████╗")
print(" ██╔══██║██║╚██╔╝██║██╔══██║██║  ██║██╔══╝  ██║   ██║╚════██║")
print(" ██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝███████╗╚██████╔╝███████║")
print(" ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝  (Ver.2.1)")
print("")
print ("** STRATOS LABS **")
print ("** 2020 **")
print("")
print("")

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 
