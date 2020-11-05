import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import wikipedia #pip install wikipedia
import os
import random
import smtplib

email={"abc":"vrushalitandel2@gmail.com","xyz":"vrushalitandel1@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

## goto

engine.setProperty('voices', voices[1].id)
#id=0

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
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query1}\n")
        return query1

    except Exception:
        print("Say that again please...")
        return "None"

def sendEmail(to,msg):
    file1 = open("C:\\Users\\Dell\\Desktop\\SGP-7sem\\p.txt", "r")
    password=file1.read()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("vrushalitandel2@gmail.com",password)
    server.sendmail("vrushalitandel2@gmail.com",to,msg)
    server.close()


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
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'game' in query:
            os.system("python games.py")

        elif 'send email' in query:
            try:
                speak("Whom should i send?, Tell me the name of a person.")
                name="none"
                while name=="none":
                    name = takecommand().lower()
                    if name not in email:
                        name="none"
                        speak("I coudn't find the Person name,Say that again please")
                    else:
                        to = email[name]

                speak("What should i say?")
                text="None"
                while text=="None":
                    speak("Cannot be none")
                    text = takecommand()

                msg="none"
                speak("Do you want to add Subject??say yes or no")
                while msg == "none":
                    sub=takecommand().lower()
                    if sub == "no":
                        msg = text
                    elif sub == "yes":
                        speak("Tell me the subject!")
                        Subject="none"
                        while Subject=="none":
                            Subject = takecommand().lower()
                            if Subject=="none":
                                speak("I Coudn't recognize,Please say that again")
                        msg = 'Subject: {}\n\n{}'.format(Subject, text)

                print("Sending...")
                speak("Sending, Please wait")
                sendEmail(to, msg)
                speak("Email has been sent!")

            except Exception:
                speak("There is an error occured and email has not been sent!")


        elif query!="none" and 'exit' not in query:
            speak("searching...")
            query = query.replace("on google", "").replace("search", "")
            webbrowser.open(f'https://www.google.com/search?q={query}')

        elif 'exit' in query:
            exit()
