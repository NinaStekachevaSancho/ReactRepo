from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import logging
import docker

#enter credentials
account_name = 'surveydemo9eef'
account_key = '8mID3fQ3QT40iePKfKy7Yi2gnmnvIuKHpe5b9MU3oCmkVLnBAYNW/EsbIt1dUhTD9Pt/WBQBNOdF+AStEu/1Ow=='
container_name = 'audios'

#create a client to interact with blob storage
connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

#use the client to connect to the container
container_client = blob_service_client.get_container_client(container_name)

from azure.storage.blob import BlobServiceClient
import io

def upload_to_blob(file_name, data):
    try:
        logging.info(f"Uploading file to blob storage {account_name}...")
        blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net')
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        # Subir el archivo
        blob_client.upload_blob(data, overwrite=True)
        return blob_client.url
        logging.info("File uploaded successfully")
    except:
        logging.info("File couldn't be uploaded")

def get_blob_data(blob_name):
    try:
        logging.info("Getting the blob data...")
        # Crear un cliente de servicio Blob
        connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Obtener el cliente de blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Descargar el contenido del blob
        blob_data = blob_client.download_blob()
        return blob_data
    except Exception as e:
        logging.info(f"Error al obtener el blob: {e}")
        return None

def convert_webm_to_wav(webm_data, output_wav_path):
    client = docker.from_env()
    image_name = "linuxserver/ffmpeg:latest"

    try:
        # Ejecutando un contenedor con la imagen especificada
        # Aquí se asume que tu contenedor 'ffmpeg' toma comandos a través de la línea de comandos
        # Adapta los argumentos según tus necesidades
        response = client.containers.run(image_name, "ffmpeg -version", remove=True)
        return response.decode("utf-8")
    except docker.errors.ContainerError as e:
        print(f"Error al ejecutar el contenedor: {e}")
    except docker.errors.ImageNotFound:
        print(f"Imagen no encontrada: {image_name}")
    except docker.errors.APIError as e:
        print(f"Error de la API de Docker: {e}")


