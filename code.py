import datetime
import time
import wikipedia
import pyttsx3
import webbrowser
import os
import platform
import tkinter
from pynput.keyboard import Key,Controller
from pynput.mouse import Button,Controller
import speech_recognition as sr
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Starting All System")
    date=str(datetime.datetime.now().strftime("%A-%d-%B-%Y"))
    print(date)
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    starttime=datetime.datetime.now().strftime("%H hours and%M minutes")
    speak(f"Today is {date} and the time is {starttime}Sir!!")

    speak("I am Jarvis. Ready to accept commands")
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1.0
        audio = r.listen(source,phrase_time_limit=4)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")  

    except Exception as e:
        #print(e)
        print("Say that again...")
        return "None"
    return query    
if __name__ == "__main__":
    window=tkinter.Tk()
    wishMe()
    while True:
        query=takeCommand().lower()
        keyboard=Controller()
        #Main Logic of jarvis

        #Search something on wikipedia code
        if 'wikipedia' in query:
            speak("Searching.....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia...")
            speak(results)
        
        #Hello jarvis code    
        elif "hi jarvis" in query:
            speak("Hello Sir!!")
        
        #listen jarvis code
        elif "listen jarvis"in query:
            speak("Yes Sir!!!")
        
        #Search something on chrome code
        elif 'search jarvis' in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            time.sleep(1)
            speak("What should i search sir!!!")
            input=takeCommand()
            keyboard.type(input)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            speak("Here are the results sir!!!!")
        
        #Open a website code
        elif 'open website jarvis' in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            time.sleep(1)
            speak("Which website should I open sir!!!")
            input=takeCommand()
            keyboard.type(input)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        
        #playing music code
        elif 'play music jarvis' in query:
            music_dir="F:\\songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            
            


        #time telling code
        elif "what's the time jarvis"in query:
            starttime=datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir,The Time is{starttime}")
        
        #opening an window application code
        elif "open an app jarvis" in query:
            keyboard.press(Key.cmd)
            keyboard.release(Key.cmd)
            time.sleep(1)
            speak("which app should i open sir!!")
            input=takeCommand()
            keyboard.type(input)
            time.sleep(1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        
        #Typing something on the file code
        elif "jarvis start typing" in query:
            speak("ohk sir!!")
            time.sleep(1)
            input=takeCommand()
            keyboard.type(input)

        #Exiting jarvis code
        elif "rest jarvis" in query:
            speak("Bye Sir!!")
            exit()

        #Shutdown the system code    
        elif "shutdown the system jarvis" in query:
            speak("Ohk Sir!!!")
            os.system("shutdown /s /t 1")

         #restarting the system code   
        elif "restart the system jarvis" in query:
            speak("Ohk Sir!!!")
            os.system("shutdown /r /t 1")

        #logout the system code
        elif "logout the system jarvis" in query:
            speak("Ohk Sir!!!")
            os.system("shutdown -l")

        #key press code
        elif "perform action jarvis" in query:
            speak("which action sir!!")
            input=takeCommand()
            if "pause" or "play" in input:
                keyboard.press(Key.pause)
                keyboard.release(Key.pause)
            
        #mouse movement
        mouse=Controller()
        if "move up jarvis" in query:
            mouse.move(0,-10)
        elif "move left jarvis" in query:
            mouse.move(-10,0)
        elif "move down jarvis" in query:
            mouse.move(0,10)
        elif "move right jarvis" in query:
            mouse.move(10,0)
        elif "move up and go right jarvis" in query:
            mouse.move(0,-10)
            mouse.move(10,0)
        elif "move up and go left jarvis" in query:
            mouse.move(0,-10)
            mouse.move(-10,0)
        elif "move down and go right jarvis" in query:
            mouse.move(0,10)
            mouse.move(10,0)
        elif "move down and go left jarvis" in query:
            mouse.move(0,10)
            mouse.move(-10,0)
        elif "select item jarvis" in query:
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif "open it jarvis"in query:
            mouse.click(Button.left,2)
        elif "show options jarvis" in query:
            mouse.press(Button.left)
            mouse.release(Button.left)
            mouse.press(Button.right)
            mouse.release(Button.right)
        elif "scroll it jarvis" in query:
            mouse.scroll(0,2)
    window.mainloop()