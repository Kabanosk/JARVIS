import pyttx3

class Bot:
    engine = pyttx3.init()

    def __init__(self, name, owner, language):
        self.name = name
        self.owner = owner
        self.language = language


    def say_hello(self):
        self.engine.say(f'Hello Mr {self.owner}')
        self.engine.runAndWait()
