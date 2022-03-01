import pyttsx3

class Bot:
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    def __init__(self, name, owner, language):
        self.name = name
        self.owner = owner
        self.language = language
        self.say_hello()

    def say_hello(self):
        self.engine.say(f'Hi {self.owner}')
        self.engine.runAndWait()

    def simple_answer(self):
        self.engine.say('I am searching')
        self.engine.runAndWait()
