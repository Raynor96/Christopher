import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

with oracledb.connect(user=username, password=password, dsn=host) as connection:
       with connection.cursor() as cursor:
          sql = "select sysdate from dual"
          for r in cursor.execute(sql):
             print(r)


def create_schema():

    tables = [
        (
        "("
        "CREATE TABLE Mascota ("
        "id_mascota INT PRIMARY KEY,"         
        "edad INT,"
        "especie VARCHAR(255),"
        "historialMedico VARCHAR(255)"
        ")"

        );
        
        (
        "CREATE TABLE Perro (
        "id_mascota INT PRIMARY KEY,          
        "historialVacunas VARCHAR(255),
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)
);
   )

(
        "CREATE TABLE Ave ("
        "id_mascota INT PRIMARY KEY,"          
        "tipoJaula VARCHAR(255),"
        "controlVuelo BOOLEAN,"
        "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)"
);
)