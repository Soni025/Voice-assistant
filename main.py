import smtplib
import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import datetime

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # Without this command, speech will not be audible to us.
    engine.setProperty('voice', voices[0].id)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am an A I Sir. Please tell me how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open pinterest' in query:
            webbrowser.open("pinterest.com")
        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com/in/")
        elif 'open telegram' in query:
            webbrowser.open("https://desktop.telegram.org/")
        elif 'open erp portal' in query:
            webbrowser.open("https://igdtuw.in/IGDTUW/login")
        elif 'open discord' in query:
            webbrowser.open("https://discord.com/channels/@me")
        elif 'open zoom' in query:
            codePath = "C:\\Users\\sonis\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
        elif 'open vs code' in query:
            codePath = "C:\\Users\\sonis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open webex' in query:
            codePath = "C:\\Users\\sonis\\AppData\\Local\\CiscoSparkLauncher\\CiscoCollabHost.exe"
            os.startfile(codePath)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to soni' in query:
            try:
                speak("What should I write ?")
                content = takeCommand()
                to = "sonisharma25052005@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry soni sharma . I am not able to send this email")
        elif 'quit' or 'terminate' or 'stop' or 'exit' in query:
            sys.exit(0)

