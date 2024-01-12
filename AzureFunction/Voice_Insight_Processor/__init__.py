import base64
import datetime
import json
import uuid
import tempfile
import logging
from utils.sql_connection import *
import azure.functions as func
from Voice_Insight_Processor.WhisperAudioProcessor import generate_text
from Voice_Insight_Processor.blobl_storage_connect import upload_to_blob, convert_webm_to_wav, get_blob_data
from Voice_Insight_Processor.audio_processing import get_resume, get_leanguege, get_translation, get_sentiment, audio_response
#import sys
#sys.path.append("../")

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    try:
        # Obtener y procesar el archivo .webm del cuerpo de la solicitud
        webm_data = req.get_body()
        try:
            parsed_json = json.loads(webm_data.decode('utf-8'))

            campaign_id = parsed_json.get("campaign_id")
            rating = parsed_json.get("rating")
            logging.info("todo bien :)")
            # Extraer el audio, campaign_id y rating del JSON
            base64_audio = parsed_json.get("audio")
            if base64_audio:
                base64_audio = base64_audio[0]["Value"]  # Asegúrate de que esta estructura corresponde con tus datos
                audio_response(base64_audio)
            else:
                logging.info("Audio data not found.")
            
        except Exception as e:
            logging.error(f"Error processing request: {e}")
            # Manejar el error o devolver una respuesta HTTP adecuada

        
        # Extraer solo la parte de datos Base64 (eliminar el prefijo de tipo MIME)
        base64_string = base64_audio.split(",")[1]

        # Decodificar la cadena Base64 en bytes
        audio_bytes = base64.b64decode(base64_string)
        # Subir el archivo .webm a Blob Storage
        file_name_webm = f"archivo_{uuid.uuid4()}.webm"
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.webm', dir='/tmp') as temp_file:
                temp_file.write(audio_bytes)
                file_path = temp_file.name
        except:
            logging.error("Can not write bytes in a file")

        url = upload_to_blob(file_name_webm, audio_bytes)
        logging.info(f"--> URL Generated: {url}")
        #file_webm = get_blob_data(file_name_webm)
            #file_name = f"archivo_{uuid.uuid4()}.wav"
        try:
            with open(file_path, "rb") as file:
                logging.info("Trying to transcript...")
                try:
                    transcription = generate_text(file).text
                    logging.info(f"Transcription: {transcription}, {type(transcription)}")
                except Exception as e:
                    logging.error(f"Error during transcription: {e}")
                    return func.HttpResponse(f"Error al procesar el archivo: {str(e)}", status_code=500)
                #time.sleep(2)
                language = get_leanguege(transcription)
                logging.info(f"--> Language: {language}, {type(language)}")
                #time.sleep(2)
                translation = get_translation(transcription, language)
                logging.info(f"--> Translation: {translation}, {type(translation)}")
                #time.sleep(2)
                sentiment = get_sentiment(translation)
                logging.info(f"--> Sentiment: {sentiment}, {type(sentiment)}")
                #time.sleep(2)
                summary = get_resume(translation)
                logging.info(f"--> Summary: {summary}, {type(summary)}")
                date = datetime.datetime.now()
                # Upload to db
                # Suponiendo que row_data es una lista o tupla que contiene los datos de la fila completa
                row_data = [int(campaign_id), int(rating), transcription, translation, summary, url, sentiment, date, language]

                # Upload to db
                conn, cursor = get_sql_connection()
                insert_query = f"INSERT INTO {TABLE_NAME} (campaign_id, rating, transcription, translation, summary, audio_link, sentiment, date, language) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
                try:
                    # Ejecutar la consulta
                    cursor.execute(insert_query, row_data)
                    # Confirmar la transacción
                    conn.commit()
                    logging.info("Data uploaded to Database.")
                except Exception as e:
                    logging.error(f"Error al insertar en la base de datos: {str(e)}")
                    # Opcional: Revertir la transacción en caso de error
                    conn.rollback()
                finally:
                    # Cerrar el cursor y la conexión
                    cursor.close()
                    conn.close()

                data = {
                    "transcription": transcription,
                    "language": language,
                    "translation": translation,
                    "summary": summary,
                    "sentiment":sentiment
                }
                json_data = json.dumps(data, indent=4)
                return func.HttpResponse(json_data)
        except Exception as e:
            logging.error(f"Error during transcription: {e}")
        return func.HttpResponse(f"Error al procesar el archivo: {str(e)}", status_code=500)


    except Exception as e:
        logging.error("Something is wrong")
        return func.HttpResponse(f"Error al procesar el archivo: {str(e)}", status_code=500)
    

    # try:
    #     # Obtener el audio codificado en base64 del cuerpo de la solicitud
    #     base64_audio = req.get_body()

    #     # Decodificar base64 a bytes
    #     audio_bytes = base64.b64decode(base64_audio)

    #     # Crear un buffer de memoria con los datos de audio
    #     audio_buffer = io.BytesIO(audio_bytes)

    #     # Escribir los datos en un archivo temporal (aquí se puede usar un nombre de archivo único)
    #     logging.info('Saving in tmp...')
    #     temp_input = '/tmp/temp_input'
    #     temp_output = '/tmp/temp_output.wav'
    #     with open(temp_input, 'wb') as file:
    #         file.write(audio_buffer.getvalue())

    #     # Comando para ejecutar ffmpeg y convertir el archivo a formato WAV
    #     command = ['ffmpeg', '-i', temp_input, temp_output]

    #     # Ejecutar el comando ffmpeg
    #     subprocess.run(command, check=True)

    #     # Leer el archivo WAV resultante y devolverlo como respuesta HTTP
    #     with open(temp_output, 'rb') as file:
    #         wav_data = file.read()

    #     return func.HttpResponse(wav_data, status_code=200)

    # except Exception as e:
    #     return func.HttpResponse(f"Error al procesar el audio: {str(e)}", status_code=500)



    # logging.info('Python HTTP trigger function processed a request.')

    # # Comando de ejemplo para ejecutar ffmpeg
    # command = ["ffmpeg", "-h"]

    # try:
    #     byte_output = subprocess.check_output(command)
    #     logging.info('AAAAAAA')
    #     return func.HttpResponse(byte_output.decode('UTF-8').rstrip(), status_code=200)
    # except Exception as e:
    #     logging.info('BBBBBB')
    #     return func.HttpResponse(f"Error al ejecutar ffmpeg: {str(e)}", status_code=500)