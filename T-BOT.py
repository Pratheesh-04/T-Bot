import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import wikipedia
from gtts import gTTS
from playsound import playsound
import os

text = "enter 0 for tamil, 1 for hindi, 2 for english... "
speak = gTTS(text=text, lang="en", slow=False)
speak.save("captured_voice1.mp3")
playsound("captured_voice1.mp3")
os.remove("captured_voice1.mp3")
 
n = int(input())

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)

if n == 0:
    text = "en peyer genie .Taṅkaḷukku eṉṉa utavi ventum"
    speak = gTTS(text=text, lang="ta", slow=False)
    speak.save("captured_voice.mp3")
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')

    def talk(text):
        translator = Translator()
        text_to_translate = translator.translate(text, dest="ta")
        text = text_to_translate.text
        speak = gTTS(text=text, lang="ta", slow=False)
        speak.save("captured_voice.mp3")
        print(text)
        playsound('captured_voice.mp3')
        os.remove('captured_voice.mp3')


    def take_command():
        # try:
        with sr.Microphone() as source: 
            print("listening")
            voice = listener.listen(source) 
            print("voice listened")
            command = listener.recognize_google(voice, language= 'ta-IN')
            translator = Translator()
            text_to_translate = translator.translate(command, dest="en")
            c = text_to_translate.text
            d = c.lower()
                    
            if 'who is' in d:
                person = d.replace('who is', '')
                info = wikipedia.summary(person, 1)
                talk(info)
                
    take_command()
    
elif n==1:
    text = "mera naam genie hai, main tumhaare lie kya kar sakata hoon?"
    speak = gTTS(text=text, lang="hi", slow=False)
    speak.save("captured_voice.mp3")
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')

    def talk(text):
        translator = Translator()
        text_to_translate = translator.translate(text, dest="hi")
        text = text_to_translate.text
        speak = gTTS(text=text, lang="hi", slow=False)
        speak.save("captured_voice.mp3")
        print(text)
        playsound('captured_voice.mp3')
        os.remove('captured_voice.mp3')


    def take_command():
        # try:
        with sr.Microphone() as source: 
            print("listening")
            voice = listener.listen(source) 
            print("voice listened")
            command = listener.recognize_google(voice, language= 'hi-IN')
            translator = Translator()
            text_to_translate = translator.translate(command, dest="en")
            c = text_to_translate.text
            d = c.lower()
                    
            if 'who is' in d:
                person = d.replace('who is', '')
                info = wikipedia.summary(person, 1)
                talk(info)
                
    take_command()


else:
    text = "my name is genie. what can i do for you?"
    speak = gTTS(text=text, lang="en", slow=False)
    speak.save("captured_voice.mp3")
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')

    def talk(text):
        translator = Translator()
        text_to_translate = translator.translate(text, dest="en")
        text = text_to_translate.text
        speak = gTTS(text=text, lang="en", slow=False)
        speak.save("captured_voice.mp3")
        print(text)
        playsound('captured_voice.mp3')
        os.remove('captured_voice.mp3')
        


    def take_command():
        # try:
        with sr.Microphone() as source: 
            print("listening")
            voice = listener.listen(source) 
            print("voice listened")
            command = listener.recognize_google(voice, language= 'en-IN')
            translator = Translator()
            text_to_translate = translator.translate(command, dest="en")
            c = text_to_translate.text
            d = c.lower()
                    
            if 'who is' in d:
                person = d.replace('who is', '')
                info = wikipedia.summary(person, 1)
                talk(info)
                
    take_command()
