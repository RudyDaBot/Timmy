import speech_recognition as recognizer
import pyttsx3


print("Initializing speech recognizer")
r = recognizer.Recognizer()

print("Setting up speech synthesis")
synthesis = pyttsx3.init()
synthesis.setProperty('rate', 130)

def speak (speechParam) :
    synthesis.say(speechParam)
    synthesis.runAndWait()

def commandsMain (input) :
    if input == "how are you" : 
      print("I am fine, thanks for asking!")
      speak("I am fine, thanks for asking!")
    
    if input == "what is your name" : 
     print("My name is TIMMY. The Technically Intelligent Miniature Manly Youth.")
     speak("My name is TIMMY. The Technically Intelligent Miniature Manly Youth.")

    if input == "who created you" :
      print("My creator is RudyDaBot")
      speak("My creator is RudyDaBot")