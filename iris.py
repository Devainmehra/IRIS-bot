import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') # sapi5 is used to give voices from windows in the program
voices = engine.getProperty('voices') 
engine.setProperty('voices',voices[1].id) # for selecting voice of id having 1 
# print(voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morning")
   elif hour>=12 and hour<18:
      speak("Good Afternoon")
   else:
      speak("Good Evening")
   speak("My name is Iris. How can I help you")
def takeCommand():
   # it takes miccrophone i/p from user and return string o/p
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening......")
      r.pause_threshhold = 1
      audio = r.listen(source)
      
   try:
      print("Recognizing....")
      query = r.recognize_google(audio, language='en-in')
      print(f"user said: {query}\n")
   
   except Exception as e:
      print("Say that again please....")
      return "None"
   return query

def sendEmail(to,content):
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login('devainmehra7@gmail.com','devain123456')
   server.sendmail('devainmehra7@gmail.com',to,content)
   server.close()


if __name__ == "__main__" :
   wishMe()
   while True:
      query = takeCommand().lower()

   # speak("NONE")
      if 'wikipedia' in query:
         speak('Searching Wikipedia ....')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=2)
         speak("According to Wikipedia")
         print(results)
         speak(results)
      
      elif 'open youtube' in query:
         webbrowser.open("youtube.com")
      
      elif 'open Google' in query:
         webbrowser.open("google.com")

      elif 'open netflix' in query:
         webbrowser.open("netflix.com")
      
      elif 'open prime' in query:
         webbrowser.open("prime.com")

      elif 'open spotify' in query:
         webbrowser.open("spotify.com")

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir,the time is {strTime}")
      elif 'open code' in query:
         codepath = "C:\\Users\\asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
         os.startfile(codepath)

      elif 'email to deva' in query:
         try:
            speak("What should i say?")
            content = takeCommand()
            to = "devainmehra0@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")
         except Exception as e:
            print(e)
            speak("Sorry email could not be sent , You can check the issue and try to resend it again ")

