import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

with oracledb.connect(user=username, password=password, dsn=dsn) as connection:
    with connection.cursor() as cursor:
        sql = "select sysdate from dual"
        for r in cursor.execute(sql):
            print(r)


def create_schema_all():

    tables = [

        (
            "CREATE TABLE Mascota ("
            "id_mascota INT PRIMARY KEY, "
            "edad INT, "
            "especie VARCHAR2(255), "
            "historialMedico VARCHAR2(255)"
            ")"
        ),

        (
            "CREATE TABLE Perro ("
            "id_mascota INT PRIMARY KEY, "
            "historialVacunas VARCHAR2(255), "
            "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
            ")"
        ),

        (
            "CREATE TABLE Ave ("
            "id_mascota INT PRIMARY KEY, "
            "tipoJaula VARCHAR2(255), "
            "controlVuelo CHAR(1) CHECK (controlVuelo IN ('S','N')), "
            "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
            ")"
        ),

        (
            "CREATE TABLE Gato ("
            "id_gato NUMBER PRIMARY KEY, "
            "esterilizado CHAR(1) CHECK (esterilizado IN ('S','N')), "
            "CONSTRAINT fk_gato_mascota "
            "FOREIGN KEY (id_gato) REFERENCES Mascota(id_mascota) "
            "ON DELETE CASCADE"
            ")"
        )
    ]

    for query in tables:
        create_schema(query)


create_schema_all()