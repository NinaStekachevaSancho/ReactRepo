import os
from openai import AzureOpenAI
import logging
from dotenv import load_dotenv
load_dotenv()

model = os.getenv("WHISPER_MODEL")

client = AzureOpenAI(
  api_key = "32f0693d7cba490f84d540f23f74543a",  
  api_version = "2023-09-01-preview",
  azure_endpoint ="https://oai-survey-dev-usnorth-001.openai.azure.com/",

)

def generate_text(wave_file):
  logging.info("Generating the transcription")
  transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=wave_file,
  )
  return transcript

def completion(text):
  response = client.chat.completions.create(
    model="test",
    messages=text
  )
  return response.choices[0].message.content