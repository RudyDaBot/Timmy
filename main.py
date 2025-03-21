import core
import os
import speech_recognition as sr
import pyttsx3
import time
import json

debugMode = bool(input("Enter Debug Mode? : "))

with open('config.json', 'r') as file: 
  config = json.load(file)
  if debugMode : 
    print(config)


contextual = config['initialContext']
print("contexttual is this ", contextual)

r = sr.Recognizer()
ss = pyttsx3.init()
ss.setProperty('rate', 130)

print("Meta Llama 3.2 Internet Access Demo. Type /bye to quit, ctrl+c may not cleanly flush occupied memory")

modeOfInput = str(input("Enter mode of input, voice or text : "))


if modeOfInput == "text" : 
  print("Text Mode Active. Restart TIMMY for voice mode.")

  while(True) :
    print(">>>", end="")
    userInput=str(input(""))

    if userInput == "/bye" :
     os.system("ollama stop llama3.2")
     print("Exiting and flushing memory.")
     break
    elif userInput == "/Wipe-Context" :
     os.system("clear")
     contextual = ""
     print('Context Wiped. Reinitialized. The model has now started a new conversation.')
    elif userInput == "/k":
      pass
    else :
      print("Thinking...")
      tempDump = core.askOllamaText(contextual, userInput)
      print(tempDump)
      contextual += tempDump

elif modeOfInput == "voice" : 

  print("Voice Mode active. to exit, say (exit). ")

  while(True) : 

    
      print("Ready.")

      print("Voice Mode Active. Type 'ready' to begin.")
      modeTemp = str(input(">>>")) 

      if modeTemp == "ready" :

        try:
          with sr.Microphone() as source: 
            audio = r.listen(source)
            print(audio)
            text=r.recognize_google(audio)
            if debugMode : 
              print("Heard -> ", text)
        except:
          print("Error detected. Either your internet or your mic/way of speaking failed.")
          continue
      
      elif modeTemp == "exit" : 
        print("Exiting and flushing memory.")
        os.system("ollama stop llama3.2")
        break

      else :
        print("Thinking...")
        tempDumpVoice = core.askOllamaText(contextual, text)
        print(tempDumpVoice)
        ss.say(tempDumpVoice)
        ss.runAndWait()
        contextual += tempDumpVoice
        time.sleep(15)

