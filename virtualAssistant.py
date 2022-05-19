import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import smtplib
import webbrowser
import cv2
from requests import get


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon sir!")

    else:
        talk("Good Evening sir!")

    talk("I am Alexa. Please tell me how can I help you")

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wish_me()

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f"Sir, the time is {time}")

    elif 'who is' in command:
        person = command.replace('who is' ,'')
        info = wikipedia.summary(person, 3)
        talk('according to wikipedia')
        print(info)
        talk(info)

    elif 'open youtube' in command:
        talk('opening youtube')
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        talk('What do you want me to search on google sir ?')
        cm = take_command().lower()
        webbrowser.open(f"{cm}")

    elif 'open stackoverflow' in command:
        webbrowser.open("stackoverflow.com")

    elif 'open gmail' in command:
        talk('opening gmail')
        webbrowser.open("gmail.com")

    elif'open uni' in command:
        webbrowser.open("candidat.groupe-insa.fr/candidat")

    elif'open insta' in command:
        webbrowser.open_new_tab('instagram.com')

    elif'open whatsapp' in command:
        talk('opening whatsapp')
        wtsppath = "C:\\Users\\Yara\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(wtsppath)

    elif'open vscode' in command:
        talk('opening vscode')
        vspath = "C:\\Users\\Yara\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vspath)

    elif'open matlab' in command:
        talk('opening matlab')
        mtpath = "C:\\Program Files\\MATLAB\\R2021b\\bin\\matlab.exe"
        os.startfile(mtpath)

    elif'open firefox' in command:
        ffpath = "C:\\Users\\Yara\\AppData\\Local\\Mozilla Firefox\\firefox.exe"
        os.startfile(ffpath)

    elif'open notepad' in command:
        talk('opening notepad')
        ntpath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(ntpath)

    elif'open command' in command:
        talk('lunching cmd')
        os.system('start cmd')

    elif'open camera' in command:
        talk('opening webcam')
        cap = cv2.VideoCapture(0)
        while True:
            ret ,img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(5)
            if k==27:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif 'ip adress' in command:
        ip = get('http://api.ipify.org').text
        talk('your ip adress is' + ip)


    elif 'date' in command:
        talk('can you shut the fuck up ?')

    elif 'how is your day going' in command:
        talk('it is going good and you?')

    elif 'motivation' in command:
        talk(' youre the only one that matter dodnt give uo on your dreams')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'greetings'in command:
        talk('thank you I love you so much')

    elif 'who are you'in command:
        talk('I am alexa and you?')

    elif 'i am'in command:
        talk(' well nice to meet you')

    elif 'alarm'in command:
        talk('Enter the time please !')
        time = input(': Enter the time please :')

        while True:
            time_Ac = datetime.datetime.now()
            now = time_Ac.strftime('%H:%M:%S')

            if now == time:
                talk('time to wake up!')
                talk('alarm closed!')

            elif now>time:
                break

    elif 'email to danny' in command:
        try:
            talk("What should I say?")
            content = take_command()
            to = "youremail@gmail.com"
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry my friend danny. I am not able to send this email")

    elif'thank you' in command:
        talk('My pleasure serving you always sir! Until next time!')
        sys.exit()

    else:
        talk('can you repeat your command sir please?')

while True:
    run_alexa()

