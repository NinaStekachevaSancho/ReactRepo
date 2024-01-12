import pyodbc
import logging
import os

######## SQL ########

# Conection to SQL

TABLE_NAME = "user_response"
ID_COLUMN = "user_id"

def get_sql_connection():
    conn_str = os.getenv("SQL_DB_CONNECTIONSTRING")
    try:
        conn = pyodbc.connect(conn_str)
        return conn, conn.cursor()
    except pyodbc.Error as e:
        logging.error(f"Error connecting to SQL database: {e}")
        return None, None

def get_sql_table_details(cursor, table_name, id_col):
    if cursor is None:
        return None, None

    table_columns = run_query(cursor, f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';")
    ids = run_query(cursor, f"SELECT {id_col} FROM {table_name}")

    if table_columns is not None:
        logging.info(f'Table columns: {table_columns}')
    if ids is not None:
        logging.info(f'Id ({id_col}) values: {ids}')

    return table_columns, ids

def run_query(cursor, query):
    try:
        cursor.execute(query)
    except pyodbc.Error as e:
        logging.warning(f'Query: {query} has syntax problems or cannot be executed! Error: {e}')
        return None

    rows = cursor.fetchall()
    if not rows:
        logging.warning(f'No results were found for the request made.')
        return None

    return [item for row in rows for item in row]