# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:27:11 2021
#YGHVE2-LE2VVT5WRR
@author: team gladiator
"""
import speech_recognition as sr
import webbrowser
import pyttsx3
import wikipedia
import os
import datetime
from twilio.rest import Client
import wolframalpha
from PyQt5 import  QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from tibby import Ui_MainWindow
import sys
import os.path
import requests
from pprint import pprint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 2)



def speak(audio):
    engine.say(audio)
    #engine.iterate()
    
    engine.runAndWait()
    #engine.endLoop()
    #engine.stop()
    #externalLoop()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    assname =("Tibby")
    speak("I am your Assistant")
    speak(assname)
    #speak("How can i Help you Sir")
    
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();
	
def print_weather(result,city):
	speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	speak("with Wind speed: {} m/s".format(result['wind']['speed']))
	
def weather(weaCity):
	city=weaCity
	print()
	try:
	  query='q='+city;
	  w_data=weather_data(query);
	  print_weather(w_data, city)
	  print()
	except:
	  speak('City name not found...')    

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()
        #engine.endLoop()
        #engine.stop()
        

    def takeCommand(self):
        speak("How can i Help you Sir")    
        r3=sr.Recognizer()
        with sr.Microphone() as source:
            print('speak now')
            audio=r3.listen(source)
    
        try:
            text1=r3.recognize_google(audio)
            print("you said:",text1)
        except sr.UnknownValueError:
            speak("could not understand audio")
        except sr.RequestError as e:
            speak("could not request results; (0)",format(e))
            
        return text1
    
    #if __name__ == '__main__':
    
    
    
    def TaskExecution(self):    
        clear = lambda: os.system('cls')
         
        wishMe()
        clear()
        
         
        while True:
            
            self.text = self.takeCommand().lower()
            #speak("Good Evening Sir !") 
            
            speak(" You said"+ self.text)
            if 'Wikipedia' in self.text:
                speak('Searching Wikipedia...')
                query = self.text.replace("wikipedia", "")
                results = wikipedia.summary(self.text, sentences = 2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                
            elif 'time card' in self.text:
                speak("Opening Oracle and Field glass")
                webbrowser.open("https://ebiz-prod.tibco.com")            
                webbrowser.open("https://www.fieldglass.net/worker_desktop.do")
                
            elif 'open lms' in self.text:
                speak("Opening Leave management system")
                webbrowser.open("https://cloud.emsphere.com/Empower_Ent_Tibco/app")                
                
           
    
            elif "tibby" in self.text:
                wishMe()
                speak("tibby at your service Mister")
            
            elif 'open notepad plus plus' in self.text:
                notepadPath = r"C:\Program Files\Notepad++\notepad++.exe"
                os.startfile(notepadPath)
            
            
            elif 'how are you' in self.text:
                speak("I am fine, Thank you")
                #speak("How are you, Sir")
                
            elif 'fine' in self.text or "good" in self.text:
                speak("It's good to know that your fine")    
                
            elif "who made you" in self.text:
                speak("I was made by team gladiators for the hackathon")
                
            elif 'bye bye' in self.text or 'bye-bye' in self.text:
                speak("Bye Bye sir,Have a good day")
                exit()    
            
            elif 'weather' in self.text:
                city = self.text.replace("what is the weather in","")
                print(city)
                speak("Here is the weather of "+ city)
                weather(city)
                
            elif 'how were you made' in self.text:
                speak("Confidential information access denied")
            
            elif 'anything else to say' in self.text:
                speak("Yes sir, I would like to request everyone to vote for team gladiators for the hackathon")
                
            
            elif "what is" in self.text or "who is" in self.text:
                client = wolframalpha.Client("YGHVE2-LE2VVT5WRR")
                res = client.query(self.text)
                try:
                    print (next(res.results).self.text)
                    speak (next(res.results).self.text)
                except StopIteration:
                    print ("No results")
                    
            else:
                results = wikipedia.summary(self.text, sentences = 2)
                query = self.text.replace("wikipedia", "")
                speak("According to Wikipedia")
                print(results)
                speak(results)
                #speak("Here you go to"+ self.text)
                #webbrowser.open("https://"+ self.text +".com")
    
    
                
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        print("Hi")
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        print("2")
        self.ui.movie = QtGui.QMovie("images/giphy.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        #timer.timeout.connect(self.showTime)
        timer.start(1000)
        print("Hello")
        speak("Hi")
        startExecution.start()
        
app = QApplication(sys.argv)
Hackathon = Main()
Hackathon.show()
sys.exit(app.exec_())        