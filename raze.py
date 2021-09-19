import random
import sys
import time
from cv2 import data
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import webbrowser
import smtplib
import pyjokes
import pyautogui
import PyPDF2
from bs4 import BeautifulSoup
# import geocoder
# import pytz
import pywhatkit as kit
from requests import get
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from wikipedia.wikipedia import search
from razeUi import Ui_razeUi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if 0 <= hour <= 12:
        speak(f"Good Morning, its {tt}")
    elif 12 <= hour <= 18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    speak("I am Sage sir, please tell me how may i help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("srcottage00@gmail.com", "Yash2874$")
    server.sendmail("sparsh.tiwariy@gmail.com", to, content)
    server.close()


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8f6e5597c89a463f8881e4bf36bee3a1'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"Today's {day[i]} news is {head[i]}")


def pdf_reader():
    book = open('SR COTTAGE PP.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total Number of pages in this book {pages}")
    speak("Sir please enter the page number I have to read for you")
    pg = int(input("Please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        # self.TaskExecution()
        speak("Please say correct password to proceed")
        while True:
            self.command = self.takecommand()
            if "wake up buddy" in self.command or "are you there" in self.command:
                self.TaskExecution()
            elif "goodbye buddy" in self.command:
                speak("Thanks for using me sir, have a good day.")
                sys.exit()
            else:
                speak('wrong passwrod')

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said {query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query

    def TaskExecution(self):
        wish()
        while True:

            self.command = self.takecommand().lower()

            if 'open notepad' in self.command:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'close notepad' in self.command:
                speak("Okay sir, closing Notepad")
                os.system("taskkill /f /im notepad.exe")

            elif 'open command prompt' in self.command:
                os.system("start cmd")

            elif 'open camera' in self.command:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'play music' in self.command:
                music_dir = "C:\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'ip address' in self.command:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP Address is {ip}")

            elif 'wikipedia' in self.command:
                speak("searching wikipedia")
                command = self.command.replace("wikipedia", "")
                results = wikipedia.summary(command, 2)
                speak("According to Wikipedia")
                speak(results)

            elif 'open youtube' in self.command:
                webbrowser.open("youtube.com")

            elif 'open facebook' in self.command:
                webbrowser.open("facebook.com")

            elif 'open instagram' in self.command:
                webbrowser.open("instagram.com")

            elif 'open stackoverflow' in self.command:
                webbrowser.open("www.stackoverflow.com")

            elif 'open google' in self.command:
                speak("sir, what should i search for you?")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif 'send message' in self.command:
                kit.sendwhatmsg("+919406684367", "dummy message", 9, 10)

            elif 'play' in self.command:
                song = self.command.replace("play", "")
                speak("playing" + song)
                pywhatkit.playonyt(song)

            elif 'send email' in self.command:
                try:
                    speak("what should i say sir?")
                    content = self.takecommand().lower()
                    to = "sparsh.tiwariy@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent to Sparsh")

                except Exception as e:
                    print(e)
                    speak("Sorry sir, i am not able to send mail to Sparsh")

            elif 'joke' in self.command:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'switch the window' in self.command:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif 'news' in self.command:
                speak("Please wait sir, Fetching the latest news")
                news()

            elif 'take a screenshot' in self.command:
                speak("Sir, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak(
                    "Please sir hold the screen for for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, the screenshot is saved in our main folder.")

            elif 'read pdf' in self.command:
                pdf_reader()

            elif 'hide all files' in self.command or 'hide this folder' in self.command or 'visible for everyone' in self.command:
                speak(
                    "Sir Please tell me you want to hide this folder or make it visible for everyone?")
                condition = self.takecommand().lower()
                if 'hide' in condition:
                    os.system("attrib +h /s /d")
                    speak("Sir, all the files in this folder are hidden now.")

                elif 'visible' in condition:
                    os.system("attrib -h /s /d")
                    speak("Sir, all the files in this folder are now visible for everyone. I wish you are taking this "
                          "decision on you peace.")

                elif 'leave it' in condition or 'leave for now' in condition:
                    speak("ok sir")

            # elif 'where am i' or 'where are we' in self.command:
            #     speak("Wait sir, let me check")
            #     try:
            #         ipAdd = requests.get('https://api.ipify.org').text
            #         print(ipAdd)
            #         url = 'https://get.geojs.io/v1/ip/geo/171.61.19.162.json'
            #         geo_requests = requests.get(url)
            #         geo_data = geo_requests.json(url)
            #         city = geo_data['city']
            #         country = geo_data['country']
            #         speak(
            #             f"Sir i am not sure, but i think we are in {city} city of state in {country}")
            #     except Exception as e:
            #         speak(
            #             f"Sorry sir, Due to network issue i am not able to find where we are.")
            #     pass

            # elif 'where am i' or 'where are we' in self.command:
            #     ip = requests.get('http://api.ipify.org/').text
            #     location = geocoder.ip(ip)
            #     speak(location.city, pytz.country_names[location.country])

            elif 'shutdown system' in self.command:
                os.system("shutdown /s /t 5")

            elif 'restart the system' in self.command:
                os.system("shutdown /r /t 5")

            elif 'sleep system' in self.command:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif 'hello' in self.command:
                speak("Hello sir, May i help you with something")

            elif 'how are you' in self.command:
                speak("I am fine sir, what about you.")

            elif 'Thank you' in self.command:
                speak("Its my pleasure sir.")

            elif 'you can sleep now' in self.command:
                speak("Okay sir , I am going to sleep. you can call me anytime.")
                break

            speak("Sir, do you have any other work for me?")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_razeUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "../sage/download.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "../sage/tumblr_ce7d7e9e05ff652350d42c36183dc035_11702cad_500.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)


app = QApplication(sys.argv)
raze = Main()
raze.show()
exit(app.exec_())
