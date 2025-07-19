import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speak("I'm Listening")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_vosk(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry I didn't understand")
        return ""
    except sr.RequestError:
        speak("Speech Service Unavailable")
        return ""

def handle_command(command):
    if "hello" in command:
        speak("Hey, What's up?")
    elif "time" in command:
        speak(f"The time is {datetime.now().strftime("%H:%M")}")
    elif "date" in command:
        speak(f"Today's date is {datetime.now().strftime("%B %d, %Y")}")
    elif "open google" in command:
        speak("Opening google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "name" in command:
        speak("My name is Max Jr.")
    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Bye")
        exit()
    else:
        speak("Sorry I don't understand that yet.")

while True:
    command = listen()
    if command:
        handle_command(command)