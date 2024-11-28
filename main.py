from ollama import chat
from ollama import ChatResponse
import os

contextual = ""

def askOllama (context, inputQuery) :
    response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'assistant',
    'content': context
  },{
    'role': 'user',
    'content': inputQuery,
  },
])
    return response.message.content


print("Meta Llama 3.2 Internet Access Demo. Type /bye to quit, ctrl+c may not cleanly flush occupied memory")

while(True) :
  print(">>>", end="")
  userInput=str(input(""))

  if userInput == "/bye" :
     os.system("ollama stop llama3.2")
     break
  elif userInput == "/Wipe-Context" :
     os.system("clear")
     contextual = ""
     print('Context Wiped. Reinitialized. The model has now started a new conversation.')
  else :
    tempDump = askOllama(contextual, userInput)
    print(tempDump)
    contextual += tempDump
 

