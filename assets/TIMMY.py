import initializer as timmy
import time

while (True) :

    with timmy.recognizer.Microphone() as source:
     print('Ready')
     audio = timmy.r.listen(source)
     print(audio) #This is just a speech_recognition.AudioData object
     text = timmy.r.recognize_google(audio) #Speech to text google recognizer
     print(text) #This is what you actually said
    
    timmy.commandsMain(text)


