
import datetime

import speech_recognition as sr
import pyttsx3
import os
import webbrowser
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from My side"

if __name__ == '__main__':
    print('Phoebe')
    say("Hello Captain!It's Pheobe!what can i do for you?")
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube","https://www.youtube.com/"],["wikipedia","https://www.wikipedia.com/"],["google","https://www.google.com/"],["chat gpt","https://www.chatgpt.com/"],["Instagram","https://www.instagram.com/"],["friends","https://9movies.top/watch-tv/friends-39473.4868833"],["movies","https://prmovies.house/"],["whatsapp","https://web.whatsapp.com/"],]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
               say(f" Opening {site[0]} Captain...")
               webbrowser.open(site[1])

        musics = [["specials","https://open.spotify.com/track/0GWNtMohuYUEHVZ40tcnHF?si=c24d48d9c8d7481b"]]
        for music in musics:
            if music[0].lower() in query.lower():
               say(f"play {music[0]} Captain...")
               webbrowser.open(music[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour}  {min} ")

        apps = [["spotify","spotify"],["telegram",r"C:\Users\Rabina\AppData\Roaming\Telegram Desktop\Telegram"],["VS code",r"C:\Users\Rabina\AppData\Local\Programs\Microsoft VS Code\Code.exe"]]
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
               say(f"opening {app[0]} app Captain...")
               os.startfile(app[1])
