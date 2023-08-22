import speech_recognition as sr
import gtts
from playsound import playsound
import os
import time

print("Initializing speech recognizer")

r = sr.Recognizer()

while (True) :

    with sr.Microphone() as source:
     print('Ready')
     audio = r.listen(source)
     print(audio) #This is just a speech_recognition.AudioData object
     text = r.recognize_google(audio) #Speech to text google recognizer
     print(text) #This is what you actually said

    if (text == "how are you") : 
     os.system("echo I am fine, Thanks for asking!")
     t1 = gtts.gTTS('I am fine, Thanks for asking!')
     t1.save('erica.mp3')
     playsound("erica.mp3")
    
    if (text == "open task manager") : 
     t1 = gtts.gTTS('Opening task manager now.')
     t1.save('erica.mp3')
     playsound('erica.mp3')
     os.system('taskmgr')

    if (text == "exit") :
     t1 = gtts.gTTS('Exiting.')
     t1.save('erica.mp3')
     playsound("erica.mp3")
     break
     
print("Timmy has been shut down. Closing CMD Window...")
time.sleep(5)

    
  

