import azure.functions as func
import logging
from utils.sql_connection import get_sql_connection
from utils.query import get_question_by_campaign_id
#import sys
#sys.path.append("../")

# Nombre de la tabla y la columna ID en la base de datos

TABLE_NAME = "campaigns"
ID_COLUMN = "campaign_id"

# Azure Function
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Obtener el campaign_id de los parámetros de la solicitud
    campaign_id = req.params.get('campaign_id')
    if not campaign_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            campaign_id = req_body.get('campaign_id')

    # Conectar a la base de datos y obtener la pregunta
    if campaign_id:
        conn, cursor = get_sql_connection()
        if conn is not None and cursor is not None:
            question = get_question_by_campaign_id(cursor, TABLE_NAME, campaign_id)
            cursor.close()
            conn.close()

            if question:
                return func.HttpResponse(f"Question for campaign ID {campaign_id}: {question}", status_code=200)
            else:
                return func.HttpResponse(f"No question found for campaign ID {campaign_id}", status_code=404)
        else:
            return func.HttpResponse("Failed to connect to the database.", status_code=500)
    else:
        return func.HttpResponse(
            "Please provide a campaign_id in the query string or in the request body.",
            status_code=400
        )
