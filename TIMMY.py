import speech_recognition as sr
import pyttsx3
import os
import time

print("Initializing speech recognizer")
r = sr.Recognizer()

print("Setting up speech synthesis")
ss = pyttsx3.init()
ss.setProperty('rate', 130)

while (True) :

    with sr.Microphone() as source:
     print('Ready')
     audio = r.listen(source)
     print(audio) #This is just a speech_recognition.AudioData object
     text = r.recognize_google(audio) #Speech to text google recognizer
     print(text) #This is what you actually said

    if text == "how are you" : 
     os.system("echo I am fine, Thanks for asking!")
     ss.say('I am fine, thanks for asking!')
     ss.runAndWait()
    
    if text == "what is your name" : 
     ss.say('My name is TIMMY. The Technically Intelligent Miniature Manly Youth')
     ss.runAndWait()

    if text == "who created you" :
      ss.say("Rudy has created me. Check him out on GitHub. His name is RudyDaBot.")
      ss.runAndWait()

    if text == "exit" :
     ss.say('Exiting. Bye.')
     ss.runAndWait()
     break
     
print("Timmy has been shut down. Closing CMD Window...")
time.sleep(5)

    
  

