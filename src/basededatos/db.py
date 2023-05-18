#Para la conexion a Base de Datos Postgres
import psycopg2
#Capturar errores
from psycopg2 import DatabaseError
#Variables de entorno
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex