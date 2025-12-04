import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("C##christopher_ruiz")
dsn = os.getenv("192.168.50.186/xe")
password = os.getenv("inacap#2025")


def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada \n {query}")
    except oracledb.DatabaseError as error:
        print(f"No se pudo crear la tabla: {error}")

tables = [
]
for query in tables:
    create_schema(query)