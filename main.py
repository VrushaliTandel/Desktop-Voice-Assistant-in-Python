import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import wikipedia #pip install wikipedia
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if (hour >= 0) and (hour < 12):
        speak("Good Morning!")

    elif (hour >= 12) and (hour < 18):
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("please tell me How may i help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query1}\n")
        return query1

    except Exception:
        print("Say that again please...")
        return "None"


if __name__ == "__main__":
    speak("Hello,I'm ZIRA")
    wish()

    while True:
        query = takecommand().lower()

        if 'how are you' in query:
            speak("I'm fine")
            speak("How are you?")

        elif 'thank you' in query:
            speak("You're welcome")

        elif 'sorry' in query:
            speak("No Problem")

        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Right now the time is {Time}")

        elif 'date' in query:
            Date = datetime.datetime.now().strftime("%B:%d:%Y")
            speak(Date)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')

        elif 'open classroom' in query:
            webbrowser.open('https://classroom.google.com/')

        elif 'play music' in query:
            path = 'C://Users//Dell//Pictures//Sonu//Old Songs'
            songs = os.listdir(path)
            s = random.choice(songs)
            os.startfile(os.path.join(path, s))

        elif 'open camera' in query:
            path = "C://Program Files (x86)//CyberLink//YouCam//YouCam.exe"
            os.startfile(path)

        elif 'wikipedia' in query:
            speak('searching...')
            query = query.replace("wikipedia", "").replace("search", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'game' in query:
            os.system("python -m freegames.snake")

        elif query!="none":
            speak("searching...")
            query = query.replace("on google", "").replace("search", "")
            webbrowser.open(f'https://www.google.com/search?q={query}&rlz=1C1CHBD_enIN824IN824&oq={query}&aqs=chrome..69i57j0l7.1579j0j15&sourceid=chrome&ie=UTF-8')

        elif 'exit' in query:
            exit()
