import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os

openai.api_key = api_data

completion = openai.Completion()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) # set the rate to 150 words per minute

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello, My name is SAGE. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say That Again....")
            speak("Say that again please...")

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'search' in query and 'on youtube' in query:
            try:
                search_query = query.split('search ')[1].split(' on youtube')[0]
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            except IndexError:
                speak("Sorry, I didn't catch the search query. Please try again.")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open zoro' in query:
            webbrowser.open("zoro.to")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'open gomovies' in query:
            webbrowser.open("gomovies.sx")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'who are you' in query:
            speak(f"Sir, I am an Artificial voice assistant, made by the students of CSE department at Thaapr Institute of Technology")
        elif 'what is your name' in query:
            speak(f"My name is Sage, which stands for, just a rather very intelligent software")
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'bye' in query:
            speak("Goodbye")
            break
        else:
            ans = completion.create(prompt=f'{query}\nSage: ', engine="text-davinci-002", stop=['\Sage'], max_tokens=200).choices[0].text.strip()
            print(ans)
            speak(ans)
