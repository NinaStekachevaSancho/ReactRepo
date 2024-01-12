
import json
import base64
import subprocess
import io
import os
import wave
import logging
import azure.functions as func
from Voice_Insight_Processor.WhisperAudioProcessor import generate_text, completion

# import openai
# model_engine = 'whisper-1'
# openai.api_key = "32f0693d7cba490f84d540f23f74543a"
# openai.api_base = "https://oai-survey-dev-usnorth-001.openai.azure.com/"
# openai.api_type = "azure"
# openai.api_version ='2023-09-01-preview'
# deployment_id = "whisper-1"
# language = "en"


# def generate_text(wave_file):
#     transcript = openai.Audio.transcribe(model=model_engine,
#                                         file=wave_file,
#                                         deployment_id=deployment_id,
#                                         language=language)
#     return transcript


file_name = "mi_archivo.wav"
try:
    with open(file_name, "rb") as file:
        transcription = generate_text(file)
        print(transcription)
except Exception as e:
    logging.error(f"Error during transcription: {e}")

mensaje = "Hola. qué día es hoy?"
print(completion(mensaje))

# app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
# @app.route(route="VoiceInsightProcessor")
# def VoiceInsightProcessor(req: func.HttpRequest) -> func.HttpResponse:

#     logging.info('Python HTTP trigger function processed a request.')
#     try:
#         # Obtener y procesar el archivo .webm del cuerpo de la solicitud
#         #webm_data = req.get_body()

#         # Subir el archivo .webm a Blob Storage
#         #file_name_webm = f"archivo_{uuid.uuid4()}.webm"
#         #upload_to_blob(file_name_webm, webm_data)

#         # Convertir .webm a .wav
#         data_wav = get_blob_data("test.wav")
#         logging.info(f"Type{type(data_wav)}")
#         logging.info("Success in loading data from blobstorage :)")
#         #file_name_wav = f'/tmp/{file_name_webm}.wav'
#         #success = convert_webm_to_wav(webm_data, file_name_wav)
#         success = True
#         if success:
#             file_name = "test_hindi_opinion.wav"
#             try:
#                 with open(file_name, "rb") as file:
#                     logging.info("Trying to transcript...")
#                     transcription = generate_text(file).text
#                     logging.info(f"Transcription: {transcription}, {type(transcription)}")
#                     time.sleep(2)
#                     language = get_leanguege(transcription)
#                     time.sleep(2)
#                     translation = get_translation(transcription, language)
#                     time.sleep(2)
#                     resume = get_resume(translation)
                    
#                     data = {
#                         "transcription": transcription,
#                         "language": language,
#                         "translation": translation,
#                         "resume": resume
#                     }
#                     json_data = json.dumps(data, indent=4)
                    
#             except Exception as e:
#                 logging.error(f"Error during transcription: {e}")
#             return func.HttpResponse(json_data)
#         else:
#             logging.error("Conversion to WAV failed.")


#     except Exception as e:
#         return func.HttpResponse(f"Error al procesar el archivo: {str(e)}", status_code=500)

