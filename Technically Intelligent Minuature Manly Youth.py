import speech_recognition as sr
import pyttsx3
import os
import time

print("Initializing speech recognizer")
r = sr.Recognizer()

print("Setting up speech synthesis")
speechS = pyttsx3.init()
speechS.setProperty('rate', 130)

while (True) :

    with sr.Microphone() as source:
     print('Ready')
     audio = r.listen(source)
     print(audio) #This is just a speech_recognition.AudioData object
     text = r.recognize_google(audio) #Speech to text google recognizer
     print(text) #This is what you actually said

    if (text == "how are you") : 
     os.system("echo I am fine, Thanks for asking!")
     speechS.say('I am fine, thank you!')
     speechS.runAndWait()
    
    if (text == "open task manager") : 
     speechS.say('Opening Task Manager')
     speechS.runAndWait()
     os.system('taskmgr')

    if (text == "exit") :
     speechS.say('Exiting. Bye.')
     speechS.runAndWait()
     break
     
print("Timmy has been shut down. Closing CMD Window...")
time.sleep(5)

    
  

