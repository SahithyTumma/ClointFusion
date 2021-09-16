import os
import random
import requests
import datetime
import sys
import time
import wikipedia
import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import ClointFusion as cf

#Install pyaudio
try:
    import pyaudio
except:
    sys_version = str(sys.version[0:6]).strip()
    
    py_audio_file = ""
    if "3.7" in sys_version :
        cmd = "https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Wheels/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl?raw=true"
    elif "3.8" in sys_version :
        cmd = "https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Wheels/PyAudio-0.2.11-cp38-cp38-win_amd64.whl?raw=true"
    elif "3.9" in sys_version :
        cmd = "https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Wheels/PyAudio-0.2.11-cp39-cp39-win_amd64.whl?raw=true"

    time.sleep(5)

    try:
        os.system("pip install " + cmd)
    except:
        print("Please install appropriate driver from : https://github.com/ClointFusion/Image_ICONS_GIFs/tree/main/Wheels")

    import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio)
                print(f"You Said : {query}")
                return query
                break
            except:
                print("Try Again")

def play_on_youtube():
    speak("OK...")
    speak("Which video ?")
    video_name = command().lower() ## takes user command 
    speak("Opening YouTube now, please wait a moment")
    kit.playonyt(video_name)

def send_WA_MSG():
    speak("OK...")
    speak("Whats the message")
    msg = command().lower() ## takes user command 
    speak("Got it, whom to send, please say mobile number without country code")
    num = command().lower() ## takes user command 
    speak("Sending message now, please wait a moment")

    kit.sendwhatmsg_instantly(phone_no=f"+91{num}",message=str(msg),wait_time=25, tab_close=True, close_time=5)

def google_search():
    speak("OK...")
    speak("Whats to search")
    msg = command().lower() ## takes user command 
    speak("Searching in Gooogle now, please wait a moment")

    kit.search(msg)

def greet_user():
    hour = datetime.datetime.now().hour
    greeting = "Good Morning...." if 5<=hour<12 else "Good Afternoon....." if hour<18 else "Good Evening...."
    choices = ["Hey...", "Hi...", "Hello...", "Dear..."]
    greeting = random.choice(choices) + str(cf.user_name) + "..." + greeting + "..."
    speak(greeting + "How can i assist you ?")
    queries = ["you can ask my name..","current time..","global news..","send whatsapp to someone","Send gmail..", "play youtube video...","search in google..."]
    speak("You can ask..")
    choices=random.sample(queries,len(queries))
    speak(choices)
    speak('To quit, you can say exit...quit..bye..stop')

def bol_main():

    while True:
        query = command().lower() ## takes user command 
        
        if 'name' in query:
            speak("I am ClointFusion's BOL....")

        ### time
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak("It's " + str(time))
        
        ### celebrity
        elif 'who is' in query:
            try:
                query = query.replace('who is',"")
                speak(wikipedia.summary(query,2))
            except:
                speak("Please use a complete word")

        #Send WA MSG
        elif any(x in query for x in ["send whatsapp","whatsapp","whatsapp message"]): 
            try:
                send_WA_MSG()
            except:
                speak("Sorry, i am experiencing some issues, please try later")

        #Play YouTube Video
        elif any(x in query for x in ["youtube","play video","video song","youtube video"]): 
            try:
                play_on_youtube()
            except:
                speak("Sorry, i am experiencing some issues, please try later")

        #Search in Google
        elif any(x in query for x in ["google search","search in google"]): 
            try:
                google_search()
            except:
                speak("Sorry, i am experiencing some issues, please try later")

        ### news
        elif 'news' in query:
                def trndnews(): 
                    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                    page = requests.get(url).json() 
                    article = page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)): 
                        print(i + 1, results[i]) 
                    speak("here are the top trending news....!!")
                    speak("Do yo want me to read!!!")
                    reply = command().lower()
                    reply = str(reply)
                    if reply == "yes":
                        speak(results)
                    else:
                        speak('ok!!!!')
                        pass
                trndnews() 

        elif any(x in query for x in ["bye","quit","stop","exit"]):
            speak("Have a nice day ! ")
            break

        elif "blockly" in query:
            cf.browser_activate('http://dost.clointfusion.com')

        elif "close google chrome" in query:
            cf.browser_quit_h()

        else:
            speak("I don't understand what you are saying")