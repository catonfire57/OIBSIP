# selected model is fixt/home-3b-v3:latest being the lightest in my knowledge 

import pyttsx3 
import speech_recognition as sr
from gtts import gTTS
import pygame
from io import BytesIO
import datetime
import os
#import cv2
import requests
from requests import get
import webbrowser as wb
from keyboard import press
import time
import pywhatkit as kit
import sys 
import winsound
import pyjokes  
import threading
import pyautogui
from pywikihow import search_wikihow
import psutil
import random
import geocoder
import requests
import json
import ollama
import pandas as pd
pygame.init()
pygame.mixer.init()

def wait():
    while pygame.mixer.get_busy():
        time.sleep(1)


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('rate', 190)
engine.setProperty('voice', voice[1].id)

# text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def speak_with_gtts(text, language='en', tld='co.in'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()
    wait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("RECOGNIZING...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        return ""
    return query

def read_mastername():
    global mastername
    with open("C:\\Users\\saksh\\OneDrive\\Desktop\\username.txt") as masternamefile:
        mastername = masternamefile.read().strip()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning sir, flash is online, kaya would be working in background")
    elif hour>=12 and hour<16:
        speak("good afternoon sir, flash is online, kaya would be working in background")
    else: speak("good evening sir, flash is online, kaya would be working in background")

#def set_reminder(reminder, seconds):
    #def reminder_thread():
        #speak(f"Setting a reminder for {reminder} in {seconds} seconds.")
        #time.sleep(seconds)
        #speak(f"Reminder: {reminder}")

    #thread = threading.Thread(target=reminder_thread)
    #thread.start()


def batterycheck():
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        if plugged:
            pass
        else:
            if percent<=15 and percent>10:
                speak_with_gtts("low battery, please connect the charger")
                time.sleep(400)
            if percent<=10:
                speak_with_gtts("battery is critically low, please connect the charger")
                time.sleep(300)
thread_batterycheck = threading.Thread(target=batterycheck)  # threading alarm to work in background
thread_batterycheck.daemon = True
thread_batterycheck.start()

def beep():
    global stop_beep
    stop_beep = False
    while not stop_beep:
        winsound.Beep(1200, 400)
        time.sleep(0.2)
    print("beep stopped")

stop_beep = False

def alarm(query_for_alarm):
    t = query_for_alarm.replace("wake me up after", "").replace("wake me up in", "").replace("set alarm for", "").replace("hours", "").replace("hour", "").replace("minutes", "").replace("minute", "").replace("seconds", "").replace("second", "").replace("flash", "").replace("ring the bell in", "").replace("would you", "").replace("please", "")
    t = int(t)
    if "seconds" in query_for_alarm or "second" in query_for_alarm:
        speak_with_gtts(f"sure, I'll ring the bell in {t} seconds")
        time.sleep(t)
        
    if "minutes" in query_for_alarm or "minute" in query_for_alarm:
        speak_with_gtts(f"sure, I'll ring the bell in {t} minutes")
        time.sleep(t*60)

    if "hours" in query_for_alarm or "hour" in query_for_alarm:
        speak_with_gtts(f"sure, I'll ring the bell in {t} hours")
        time.sleep(t*3600)

    beep_thread = threading.Thread(target=beep)
    beep_thread.start()         


def typewrite():
    print("INITIATING TYPEWRITE")
    while True:

        text = takecommand().lower()

        if "backspace" in text:
            pyautogui.hotkey("ctrl", "backspace")
        if "clear all" in text or "delete all" in text:
            pyautogui.hotkey("ctrl","a")
            time.sleep(1)
            pyautogui.press("backspace")
        if "stop typing" in text:
            speak("ok")
            break
        else:
            pyautogui.write(text, interval=0.1)

def screen_navigation():
    speak("initiating screen navigation")
    #speak("pls take care of any surrounding noise for better functionality")
    while True:
        q = takecommand().lower()
        if any(x in q for x in ["stop navigating", "stop navigation", "exit screen navigation", "exit navigation"]):
            speak("ok")
            break
        if "start typing" in q:
            typewrite()
        for command in commands_for_pyautogui:
            if f"press {command[0]}".lower() in q.lower():
                pyautogui.press(command[1])
            if f"hold {command[0]}".lower() in q.lower():
                pyautogui.keyUp(command[1])
            if f"release {command[0]}".lower() in q.lower():
                pyautogui.keyDown(command[1])
            if "close this window" in q:
                pyautogui.hotkey("alt", "f4")

def purge():  # clears screen...
    os.system('cls' if os.name == 'nt' else 'clear')

# def location():
#     g = geocoder.ip('me')
#     print(g.latlng)

def speak_with_random_responsegtts(key):
    response = random.choice(responses[key])
    speak_with_gtts(response)

def speak_with_random_responsepyttsx(key):
    response = random.choice(responses[key])
    speak(response)

responses = {
    "welcome": ["my pleasure master", "always ready to help sir", "no worries master", "always there for you sir"],
    "goodbye": ["kk, standbye", "goodbye sir, see you soon", "wake me up when needed sir", "thanks, I was a bit tired"],
    "joke": ["here's a joke", "I hope this makes you laugh", "my non-emotional voice is funny already, anyways here's a joke"],
    "hello": ["hello sir, I'm up", "Hi sir, what can I do for you", "I'm right here, ready to help", "I am at your service, Master.", "It's good to have you back, Master.", "It is a pleasure to see you, Master."],
    "iamup": ["I'm up and working fine", "I can't sleep without your permission hence I'm up", "I don't remember you asking me to sleep"],
    "alarm": ["knock knock, this is the alarm beep", "wake up!! it's time", "don't worry it's not system making sounds, it's me cause the alarm time is up", "Beep beep! It's time to wake up. This is your wake-up call!", "Ding ding! Wakey wakey! The alarm is going off!"],
}

commands_for_pyautogui = [
    ["!", "!"],
    ["hashtag", "#"],
    ["dollar", "$"],
    ["percentage", "%"],
    ["and", "&"],
    ["plus", "+"],
    ["0", "0"],
    ["1", "1"],
    ["2", "2"],
    ["3", "3"],
    ["4", "4"],
    ["5", "5"],
    ["6", "6"],
    ["7", "7"],
    ["8", "8"],
    ["9", "9"],
    ["colon", ":"],
    ["semi colon", ";"],
    ["lesser than", "<"],
    ["equal", "="],
    ["greater than", ">"],
    ["question mark", "?"],
    ["at the rate", "@"],
    ["add", "add"],
    ["alt", "alt"],
    ["alternate", "alt"],
    ["backspace", "backspace"],
    ["browser back", "browserback"],
    ["browser forward", "browserforward"],
    ["caps lock", "capslock"],
    ["control", "ctrl"],
    ["dot", "decimal"],
    ["point", "decimal"],
    ["delete", "delete"],
    ["divide", "divide"],
    ["down", "down"],
    ["end", "end"],
    ["enter", "enter"],
    ["escape", "escape"],
    ["F1", "f1"], ["F2", "f2"], ["F3", "f3"], ["F4", "f4"], ["F5", "f5"],
    ["F6", "f6"], ["F7", "f7"], ["F8", "f8"], ["F9", "f9"], ["F10", "f10"],
    ["F11", "f11"], ["F12", "f12"],
    ["left", "left"],
    ["multiply", "multiply"],
    ["num lock", "numlock"],
    ["page down", "pagedown"],
    ["page up", "pageup"],
    ["print screen", "prtscr"],
    ["right", "right"],
    ["separator", "separator"],
    ["shift", "shift"],
    ["shiftleft", "shiftleft"],
    ["shiftright", "shiftright"],
    ["space", "space"],
    ["subtract", "subtract"],
    ["tab", "tab"],
    ["up", "up"],
    ["volumedown", "volumedown"],
    ["mute", "volumemute"],
    ["volumeup", "volumeup"],
    ["windows", "win"],
]

sites = [

    # Entertainment & Media
    ["netflix", "https://www.netflix.com"],
    ["spotify", "https://www.spotify.com"],
    ["movie", "https://vipstream.tv"],

    # Communication & Email
    ["mailbox", "https://mail.google.com/mail/u/0/#inbox"],

    # Social Media
    ["facebook", "https://www.facebook.com"],
    ["instagram", "https://www.instagram.com"],
    ["twitter", "https://www.twitter.com"],
    ["linkedin", "https://www.linkedin.com"],

    # Educational Platforms
    ["college portal", "https://mrei.icloudems.com"],
    ["coursera", "https://www.coursera.org"],
    ["udemy", "https://www.udemy.com"],
    ["khan academy", "https://www.khanacademy.org"],

    # Productivity Tools
    ["google drive", "https://drive.google.com"],
    ["google docs", "https://docs.google.com"],

    # Shopping
    ["amazon", "https://www.amazon.com"],
    ["flipkart", "https://www.flipkart.com"],

    # Coding & Development
    ["github", "https://www.github.com"],
    ["geeksforgeeks", "https://www.geeksforgeeks.org"],

]

stop_response = False

def ai():
    model = 'fixt/home-3b-v3:latest'
    prompt = question

    try:
        stream = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
        )

        full_response = ""
        current_sentence = ""  # Accumulate content for a sentence
        for chunk in stream:
            content = chunk.get('message', {}).get('content', '')
            print(content, end='', flush=True)
            full_response += content
            current_sentence += content

            # Check for sentence boundaries (. ! ?) and speak
            if any(punct in current_sentence for punct in ['.', '!', '?']):
                speak(current_sentence.strip())  # Speak the full sentence
                current_sentence = ""  # Reset for the next sentence

        # Speak any remaining text (if the last chunk wasn't a full sentence)
        if current_sentence:
            speak(current_sentence.strip())

        print("\n")
        print(f"Full Response: {full_response}")

    except Exception as e:
        print(f"speak again..., error > {e}")


def flashthebot():   #THE MAIN PROGRAM ... !!!!!!
    
    while True:

        global stop_beep
        #global stop_response
        purge()
        query = takecommand().lower()
        assisted = False

# LOGICS FOR ALL TASKS...

        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                assisted = True
                speak("Sure, here you go")
                wb.open(site[1])


        if "notepad" in query:
            assisted = True
            speak("sure")
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2410.21.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)

        if any(x in query for x in ["start typing", "type what I say"]):
            assisted = True
            typewrite()
        
        if "cmd" in query or "command prompt" in query:
            assisted = True
            speak("sure, lesgo catto")
            os.system("start cmd")

        #if "webcam" in query:
            #cap = cv2.VideoCapture(0)
            #while True:
                #ret, img = cap.read()
                #cv2.imshow('webcam', img)
                #k = cv2.waitKey(50)
                #if k==27:
                    #break;
            #cap.release()
            #cv2.destroyAllWindows()
        
        if "my ip" in query or "the ip" in query or " ip" in query:
            assisted = True
            ip = get('https://api.ipify.org').text
            speak(ip)

        if any(x in query for x in ["hello"]):
            assisted = True
            speak_with_random_responsepyttsx("hello")

        if any(x in query for x in ["wake up", "are you up"]):
            assisted = True
            speak_with_random_responsepyttsx("iamup")
        
        if "open whatsapp" in query:
            assisted = True
            speak("ok")
            npath = "C:\\Users\\saksh\\Desktop\\flashthebot\\Shortcuts ( dont delete )\\WhatsApp.lnk"
            os.startfile(npath)
       
        if "settings" in query:
            assisted = True
            pyautogui.hotkey("win", "i")

        if "send message to" in query:
            assisted = True
            query = query.replace("send message to", "")
            person = query
            speak("what msg to send sir?")
            msg = takecommand().lower()
            if msg is not None:
                pyautogui.press("win") 
                time.sleep(1)          
                pyautogui.typewrite("whatsapp")
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(1.2)
                pyautogui.typewrite(person)
                time.sleep(1.2)
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(0.1)
                pyautogui.write(msg)
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.hotkey("alt", "f4")
                speak("done sir")
            else:
                print("speak again")
                continue


        if "chat gpt" in query:
            assisted = True
            speak("kk")
            npath = "C:\\Users\\saksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\ChatGPT.lnk"
            os.startfile(npath)

        if "open genshin" in query or "open genshin impact" in query:
            assisted = True
            npath = "C:\\Program Files\\Epic Games\\GenshinImpact\\games\\Genshin Impact game\\GenshinImpact.exe"
            os.startfile(npath)

        if any(x in query for x in ["thankyou", "thank", "crazy", "amazing"]):
            assisted = True
            speak_with_random_responsepyttsx("welcome")


        if any(x in query for x in ["search on google", "search google for", "on google", "what", "tell me", "answer", "what's", "what are", "how to", "how does", "how is", "how", "detail", "more", "who is", "calculate", "how are", "how should", "how can", "how would", "how shall", "how will", "how did", "when was", "when did", "can you", "can", "who was", "why", "would you", "may", "when", "question", "guess"]):
            if any(x in query for x in ["date", "time"]):
                if "time" in query:
                    strfTime = datetime.datetime.now().strftime("%H:%M")
                    speak(strfTime)
                    continue
                
                if "date" in query:
                    now = datetime.datetime.now()
                    date_only = now.date()
                    speak(date_only)
                    continue
                
            query = query + " answer in short"
            assisted = True
            global question
            query = query.replace("who is your master", "").replace("who made you", "").replace("who is your owner", "").replace("saksham", "").replace("kaya", "").replace("flash","")
            question = query
            ai()

        if "anime"in query:
            assisted = True
            speak("here you go weeb")
            npath = "C:\\Users\\saksh\\Desktop\\flashthebot\\Shortcuts ( dont delete )\\hianime.to.lnk"
            os.startfile(npath)

        if any(x in query for x in ["play song", "play", "play the song"]):
            assisted = True
            query = query.replace("song", "").replace("play", "").replace("the", "").replace("flash", "").replace("this", "")
            speak(f"playing {query}")
            kit.playonyt(query)

        if any(x in query for x in ["search youtube for", "search on youtube", "show youtube results for", "show results on youtube for", "on youtube"]):
            assisted = True
            query = query.replace("search youtube for", "").replace("search on youtube", "").replace("show youtube results for", "").replace("show results on youtube for", "").replace("search", "").replace("on youtube", "").replace("for", "")
            wb.open(f"https://www.youtube.com/results?search_query={query}")

        
        if any(x in query for x in ["sleep", "exit", "rest", "quit", "standby"]):
            assisted = True
            speak_with_random_responsepyttsx("goodbye")
            break
        
        if any(x in query for x in ["shutdown", "shut down", "terminate"]):
            assisted = True
            speak("terminating kaya")
            winsound.Beep(900, 500)
            sys.exit()
        
        #if "time" in query:
            #assisted = True
            #strfTime = datetime.datetime.now().strftime("%H:%M")
            #speak(strfTime)

        #if "date" in query:
            #assisted = True
            #now = datetime.datetime.now()
            #date_only = now.date()
            #speak(date_only)

        if any(x in query for x in ["parrot", "vm", "virtual machine"]):
            assisted = True
            speak("opening the parrot v m")
            npath = "C:\\Users\\saksh\\Documents\\Virtual Machines\\parrotVM\\parrotVM.vmx"
            os.startfile(npath)

        if "joke" in query:
            assisted = True
            speak_with_random_responsepyttsx("joke")
            speak(pyjokes.get_joke())

        #if "remind me" in query:
            #speak("what should I remind you for")
            #reminder = takecommand().lower()
            #speak("after what time in minutes?")
            #minute = int(input("enter time in minutes, just the number: "))
            #seconds = minute * 60
            #set_reminder(reminder, seconds)

        if any(x in query for x in ["change my window", "change window", "change this window"]):
            assisted = True         
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            speak("this?")
            while True:
                query = takecommand().lower()
                if "no" in query or "next" in query:
                    pyautogui.press("tab")
                    speak("this?")
                if "yes" in query or "ok" in query or "this" in query or "open" in query:
                    pyautogui.keyUp("alt")
                    break

        if any(x in query for x in ["switch my window", "switch window", "switch this window"]):
            assisted = True
            pyautogui.hotkey("alt", "tab")

        if any(x in query for x in ["maximize", "full screen"]):
            assisted=True
            pyautogui.hotkey("win", "up")

        if any(x in query for x in ["minimise"]):
            assisted=True
            pyautogui.hotkey("win", "down")
            time.sleep(0.1)
            pyautogui.hotkey("win", "down")

        if "screen navigation" in query:
            assisted = True
            screen_navigation()

        if "find" in query:
            query = query.replace("find", "").replace("here", "").replace("in", "").replace("this", "").replace("sheet", "").replace("document", "").replace("for me", "")
            pyautogui.hotkey("ctrl", "f")
            pyautogui.write(query)

        if "replace" in query:
            query = query.replace("with", "").replace("replace", "").replace("here", "").replace("in", "").replace("now", "")
            word1, word2 = query.split()
            pyautogui.hotkey("ctrl", "h")
            pyautogui.typewrite(word1)
            pyautogui.press("tab")
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")
            pyautogui.typewrite(word2)
            speak("check and click replace all")

        if any(x in query for x in ["close this window", "close window", "close this"]):
            assisted = True
            pyautogui.hotkey("alt", "f4")

        if any(x in query for x in ["stop", "ruk", "ruk ja", "shut up", "shutup", "shirt up", "shirtup"]):
            assisted = True
            stop_beep = True
            #stop_response = True
            speak_with_gtts("ok")

        if any(x in query for x in ["battery"]):
            assisted = True
            battery = psutil.sensors_battery()
            percent = battery.percent
            speak(f"we have {percent} percent battery right now")

        if any(x in query for x in ["alarm", "wake me", "ring"]):
            assisted=True
            query_for_alarm = query
            alarm_thread = threading.Thread(target=alarm, args=(query_for_alarm,))#   |_ this is alarm thread init
            alarm_thread.start() #                                                    |
        
        if any(x in query for x in ["introduce yourself", "who are you", "about you", "about yourself"]):
            assisted=True
            read_mastername()
            speak(f"Hello! I'm Flash, your smart and friendly assistant, here to make things easier and more fun. I work alongside Kaya, my equally brilliant partner in AI. I was developed by Saksham jain and currently working for {mastername}")
            speak("may know your name?")
            name = takecommand().lower()
            name = name.replace("hello", "").replace("flash ", "").replace("kaya ", "").replace("my ", "").replace("i am", "").replace("name ", "").replace("is ", "").replace("hi ", "").replace("myself", "").replace("this is", "").replace("I'm", "").replace("i m ", "").replace("there", "").replace("am ", "")
            speak(f"hi there {name}, it's a pleasure to meet you, is there anything i can help with?")
        
        if any(x in query for x in ["your owner", "your master", "your sir", "created you", "made you"]):
            assisted = True
            read_mastername()
            speak(f"I'm programmed by Saksham Jain and currently working for {mastername}")

        if any(x in query for x in ["remember my name", "save my name", "remember that my name", "store my name", "learn my name", "call me", "my name is", " i am "]):
            savemastername = query.replace("remember my name", "").replace("save my name", "").replace("remember that my name is ", "").replace("store my name", "").replace("learn my name", "").replace("call me", "").replace("my name is", "").replace("is ", "").replace("hello", "").replace("flash ", "").replace("kaya ", "").replace("i am ", "").replace("i m ", "").replace("i'm", "").replace("this is ", "").replace("myself ", "").replace("as ", "")
            df = pd.Series(savemastername)
            df.to_csv("C:\\Users\\saksh\\OneDrive\\Desktop\\username.txt", index=False, header=None)
            read_mastername()
            speak(f"I'd be calling you {mastername} from now")

        

if __name__ == "__main__":
    while True:
        
        purge()
        permission = takecommand().lower()
        if any(x in permission for x in ["wake up", "breakup"]):
            wish()
            flashthebot()
        if any(x in permission for x in ["terminate", "shut down", "shutdown", "kill system"]):
            speak("flash and kaya have been terminated for now")
            winsound.Beep(900, 500)
            purge()
            sys.exit()
