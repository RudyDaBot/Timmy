from ollama import chat
from ollama import ChatResponse
import json

with open('config.json', 'r') as file: 
  config = json.load(file)
  

def askOllamaText (context, inputQuery) :
    response: ChatResponse = chat(model=config['textModel'], messages=[
  {
    'role':'system',
    'content': config['systemPrompt']
  },
  {
    'role': 'assistant',
    'content': context
  },
  {
    'role': 'user',
    'content': inputQuery,
  },
])
    return response.message.content

def askOllamaVision (context, imagepath) : 
    response: ChatResponse = chat(model=config['visionModel'], messages=[
       {
          'role' : 'system',
          'content': 'Describe the following image.'
       },
       {
          
       }


    ])