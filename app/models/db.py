import psycopg2
from config import DB_CONFIG

def get_db_connection():
    """
    Establece una conexión con la base de datos utilizando los parámetros de configuración especificados en DB_CONFIG.

    Returns:
        psycopg2.connection: Objeto de conexión a la base de datos.
    
    Raises:
        psycopg2.Error: Si ocurre un error al intentar establecer la conexión.
    """
    return psycopg2.connect(**DB_CONFIG)
