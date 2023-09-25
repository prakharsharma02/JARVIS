
from ast import Break
from cProfile import label
import os
from turtle import goto
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)
#Speak function
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.\

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak(" I am jarvis . How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        speak("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
if __name__=="__main__" :
  wishme()
    
  if 1:
        query = takeCommand().lower() #Converting user query into lower case
        

        if'play music' in query:
            music_dir = 'C:\\Users\\prakh\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0   ]))

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open school website' in query:
            webbrowser.open("rrmps.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open cbse website' in query:
            webbrowser.open("cbse.nic.in")

        


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)

        elif 'jarvis define yourself' in query:
            speak("Hello,I am jarvis . I am you personal voice assistant . I can help you in many ways .")

            
            
        
        elif 'nothing' in query:
            speak("thanks for using me , have a good day")
            sys.exit

       
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching for Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
