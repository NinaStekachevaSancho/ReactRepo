import logging
import pyodbc

def get_question_by_campaign_id(cursor, table_name, campaign_id):
    if cursor is None:
        logging.error("Cursor is None. Cannot execute query.")
        return None

    try:
        query = f"SELECT question FROM {table_name} WHERE campaign_id = ?"
        cursor.execute(query, (campaign_id,))
        row = cursor.fetchone()
        if row:
            return row[0]  # Retorna el valor de la columna 'question'
        else:
            logging.warning(f"No question found for campaign_id: {campaign_id}")
            return None

    except pyodbc.Error as e:
        logging.error(f"Error executing query: {e}")
        return None
