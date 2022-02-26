import pyttx3 as ptt`

class Bot:
    def __init__(self, name, owner, language):
        self.name = name
        self.owner = owner
        self.language = language

    def say_hello(self):
        return f'Hello Mr {self.owner}'
