from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Creating ChatBot Instance

time_positive = ['what is the time right now','time','clock','what is the current time', 'what is the time now', 'what’s the time', 'what time is it',
'what time is it now', 'do you know what time it is', 'could you tell me the time, please', 'what is the time', 'will you tell me the time',
'tell me the time','time please', 'show me the time', 'what is time', 'whats on the clock', 'show me the clock',
 'what is the time','what is on the clock','tell me time','time','clock',]

time_negative = ['what are you doing', 'what’s up','when is time','who is time' 'could you', 'do you', 'what’s', 'will you', 'tell me', 'show me', 'current', 'do', 'now',
'will', 'show', 'tell','me', 'could', 'what', 'whats', 'i have time', 'who', 'who is', 'hardtime','when','what is','how',
'how is','when is','who is time','how is time','how is time','when is time']
CB = ChatBot('ChatBot',  logic_adapters=[
        #'chatterbot.logic.BestMatch',
        #'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.UnitConversion',
        'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter',
{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.75
        },
        { #here is how to call the TimeLogicAdapter when you create your own list
            'import_path': 'chatterbot.logic.TimeLogicAdapter',
            'positive': time_positive,
            'negative': time_negative
        }
        ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)
 # Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "who Developed you",
    "I am Developed by Md. Shahriar Rahman"
]
trainer = ListTrainer(CB)
trainer.train(conversation)
# # Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english',
                     'chatterbot.corpus.bangla')
# trainer_corpus.train("chatterbot.corpus.english.greetings",
#     "chatterbot.corpus.english.conversations"
# )