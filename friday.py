import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
from wikipedia.wikipedia import search
import pywhatkit
import os
import time as tt
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
# from newsapi.newsapi_client import NewsApiClient
import clipboard
import pyjokes
import string
import random
import psutil
import nltk
from examples import contacts

from tkinter import *
import pyperclip

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    if voice == 1:
        engine.setProperty("voice",voices[0].id)

    if voice == 2:
        engine.setProperty("voice",voices[1].id)
    
    speak("Hello this is friday")
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is") 
    speak(Time)    

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

# def wishme():
#     speak("Welcome back sir!")
#     time()
#     date()
#     speak("Jarvis at your service , please tell me how can i help you!")

def greeting():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        speak("Good evening sir!")
    else :
        speak("Good night sir!")                

def wishme():
    speak("welcome back sir!")
    time()
    date()
    greeting()
    speak("Jarvis at your service , please tell me how can i help you?")
# while True:  
#     voice = int(input("Press 1 for male voice\nPress 2 for female voice\n"))
    # speak(audio)
    # getvoices(voice)
# time()
# date()
# wishme()s

def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again Please...")
        return "None"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #tls= transport layer security
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone=' +phone_no+'&text='+Message)
    pyautogui.press('enter')
    sleep(10)


def searchgoogle():
    speak('What should i search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

# def news():
#     newsapi = NewsApiClient(api_key = 'e18cd1eb978840efacab7d41a57874fd')            #9e20c66e7fb14b3da227cdaff3192858
#     speak('What topic of news would you like to hear?')
#     topic = takeCommandMic()
#     data = newsapi.get_top_headlines(q = topic, language = 'en', page_size = 5)
#     newsdata = data['articles']
#     for x,y in enumerate(newsdata):
#         print(f'{x}{y["description"]}')
#         speak(f'{x}{y["description"]}')

    speak("that's it for now , i will update u in some time")

def text2speech():   #good for reading a blog
    text=clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    covid_data = f'Confirmed Cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Python\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))  
    s.extend(list(s3))  
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("Ok sir, flipping a coin")
    coin = ['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("I flipped the coin , the ressult is"+toss)

def roll():
    speak("Ok sir, rolling a dice")
    die = ['1','2','3','4','5','6']
    roll=[]
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("you got"+roll)

def cpu():
    usage = str(psutil.cpu_percent())     
    speak("CPU is at"+usage+"percent")
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak("percent")


def wifi_hello():
    root = Tk()
    root.geometry("400x400")
    pass_details = StringVar()
    myList = []

    def see_wifi_pass():
        import subprocess
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                myList.append(i)
                myList.append("--")
                myList.append(results[0])
                myList.append("|")
            except IndexError:
                myList.append(i)
                myList.append("--")
                myList.append("")

    def show_wifi_pass():
        pass_details.set(myList)


    def copytoclipboard():
        password = pass_details.get()
        pyperclip.copy(password)


    Label(root, text="Gui Wifi Password Checker", font="calibri 20 bold").pack()
    Button(root, text="Initiate Process Now", command=see_wifi_pass).pack(pady=10)
    Button(root, text="Show wifi pass details", command=show_wifi_pass).pack(pady=10)
    Entry(root, textvariable=pass_details, width=50).pack(pady=10)
    Button(root, text="Copy to clipbord", command=copytoclipboard).pack(pady=10)

    root.mainloop()



if __name__ == "__main__":
    getvoices(1)
    # wishme()
    while True:
        query = takeCommandMic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'email' in query:
            email_list = {
                'test email':'yrpqrvbgpyqyvjjwwg@sdvgeft.com'
            }
            try:
                speak("To whom do u want to send the mail")
                name = takeCommandMic()
                receiver = email_list[name]
                speak("What is the subject of the mail?")
                subject = takeCommandMic()
                speak('What should I say')
                content=takeCommandMic()
                sendEmail(receiver, subject ,content)
                speak('Email has been send')
            except Exception as e:
                print(e)
                speak('unable to end the mail')

        # elif 'message' in query:
        #     user_name = {
        #         'mama': ' +91 9419166644'
        #     }
        #     try:
        #         speak("To whom do u want to send the whatsapp message")
        #         name = takeCommandMic()
        #         phone_no = user_name[name]
        #         speak("What is the message")
        #         message = takeCommandMic()
        #         sendwhatsmsg(phone_no,message)

        #         speak('message has been send')
        #     except Exception as e:
        #         print(e)
        #         speak('unable to send the message')

        # elif 'whatsapp message' in query:
        #     speak('Whom do u want to contact?')
        #     contact = input('Recipient name : ')
        #     speak("What do u want to say?")
        #     message = input('Message : ')
        #     speak("When to send?")
        #     hour__ = int(input("Hour : "))
        #     minute__ = int(input("Minutes : "))
        #     pywhatkit.sendwhatmsg(contact,message,hour__ ,minute__)

        elif ' whatsapp message' in query:
            speak("Whom do you want to contact")
            user = takeCommandMic().lower()
            speak("What do you want to say")
            message = takeCommandMic().lower()
            speak("When to send")
            s_time = takeCommandMic().lower()
            if 'later' in s_time:
                speak("Tell me about the hour")
                hour__ = int(takeCommandMic().lower())
                speak("Tell me about the minutes")
                minutes__ = int(takeCommandMic().lower())
            elif 'now' in s_time:
                hour__ = datetime.datetime.now().hour
                if(datetime.datetime.now().second) < 30:
                    minute__ = datetime.datetime.now().minute + 1
                else:
                    minute__ = datetime.datetime.now().minute + 2
            speak("Sending message")
            pywhatkit.sendwhatmsg(contacts[user]["phone"],message,hour__ ,minute__)       

        elif 'wikipedia' in query:
            speak('Searching on wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(f'{query}', sentences = 4)
            print(result)
            speak(result)    

        elif 'google' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak('What should i search for on youtube')
            topic=takeCommandMic()
            pywhatkit.playonyt(topic)    

        elif 'weather' in query:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=jammu&units=imperial&appid=d023a30207ebf99620bbd2c743eea26b'   #2ffed89c14ec6f7fa8e3f475d84cd
            res = requests.get(url)
            data = res.json()
            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data['weather'] [0] ['description']
            temp = round((temp-32) * 5/9)
            print(weather)
            print(temp)
            print(desp)
            speak('Temperature : {} degree celcius'.format(temp))
            speak('weather is {}'.format(desp))

        elif 'news' in query:
            news()

        elif 'media' in query:
            news = wb.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions. what question do you want to ask now?')
            question=takeCommandMic()
            app_id="Paste your unique ID here "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am a robot from the future. The THF-1 version 5 point O, your personal assistant. I am programmed to minor tasks like'
                  'opening youtube. google chrome. gmail. stackoverflow. predict time. take a photo. search wikipedia. predict weather' 
                  'In different cities. get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Chiranjeev. Sorry if the pronunciation was bad")
            print("I was built by Chiranjeev. Sorry if the pronunciation was bad")

        elif "read" in query: #easy to read blogs
            text2speech()

        elif 'covid' in query:
            covid()

        elif 'documents' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))    

    #Get the proper path to vs code    
        #elif 'code' in query:
        #    codepath = 'C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.exe'
        #    os.startfile(codepath)

        elif 'joke' in query:
            myjoke = pyjokes.get_joke(language = 'en', category = 'all')
            speak(myjoke)
            print(myjoke)

        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommandMic()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt','r')
            speak("This is what you feeded in my database earlier. "+remember.read())

        elif 'generate password' in query:
            passwordgen()

        elif 'flip' in query:
            flip() 

        elif 'roll' in query:
            roll()

        elif 'cpu' in query:
            cpu()                    

        elif 'offline' in query:
            speak("Goodbye sir. Take care")
            quit()

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
			
            time.sleep(3)

        elif "tell my passwords" in query:
            speak("The following are the wifi passwords for all the modems your device has ever connected")
            wifi_hello()


#takeCommandMic == "hey jarvis what is the date today" tokenize = ['hey', 'jarvis', 'what', 'is', 'the', 'date', 'today']
