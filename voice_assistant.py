# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 00:27:54 2019

@author: Lenovo
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init("sapi5")#microsoft provide an api for speak for windows
voices=engine.getProperty("voices")
print(voices[0].id)
#engine.setProperty("voice",voices[1].id)
#print(voice)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello I am Raghs, please tell me how may i help you")
def takeCommand():# it take input through microphone and return ur command output in form string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1 # just wait 1 sec if u stop while speak before taking one cycle
        audio=r.listen(source)
    try:
        print("recorgnizing")
        query=r.recognize_google(audio,language="en_in")
        print(f"you said : {query}\n")
    except:
        print("sorry about that i didn't hear anything \nsay that again please.....")
        speak("sorry about that i didn't hear anything \nsay that again please.....")
        return "None"
    return query                             
    
         
     
if __name__ == "__main__":
    wish_me()
    while True:
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(f"wikipedia: {results}")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com") 
        elif "play music" or "open music" in query:
            music_dir="E:\download\download"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif"time enquiry" in query:
            strTime=datetime.datetime.now.strtime("%H:%M:%S")
            speak(f" Mam time is {strTime}")
        elif "open code" in query:
            codepath="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        else:
           print("sorry i can't find that")
           speak("sorry i can't find that")
            
            
            
           
            
            
            
            
    