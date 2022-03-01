import speech_recognition as sr
from bot import Bot

bot = Bot('jarvis', 'Wojtek', 'en')

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language=bot.language)
    if bot.name in text.lower():
        bot.simple_answer()
