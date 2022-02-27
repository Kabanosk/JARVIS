import speech_recognition as sr
from bot_responses import Bot

bot = Bot('javris', 'Wojtek', 'en')

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language=bot.language)
    if text.lower() == bot.name:
        bot.say_hello()

try:
    print(recognizer.recognize_google(audio, language='pl'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
