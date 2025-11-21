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


def insertar_mascota(cursor, id_mascota, edad, especie, historialMedico):
    sql = """
        INSERT INTO Mascota (id_mascota, edad, especie, historialMedico)
        VALUES (:1, :2, :3, :4)
    """
    cursor.execute(sql, (id_mascota, edad, especie, historialMedico))
    print("Mascota insertada correctamente.")


 
def insertar_perro(cursor, id_mascota, historialVacunas):
    sql = """
        INSERT INTO Perro (id_mascota, historialVacunas)
        VALUES (:1, :2)
    """
    cursor.execute(sql, (id_mascota, historialVacunas))
    print("Perro insertado correctamente.")



def insertar_ave(cursor, id_mascota, tipoJaula, controlVuelo):
    sql = """
        INSERT INTO Ave (id_mascota, tipoJaula, controlVuelo)
        VALUES (:1, :2, :3)
    """
    cursor.execute(sql, (id_mascota, tipoJaula, controlVuelo))
    print("Ave insertada correctamente.")



def insertar_gato(cursor, id_gato, esterilizado):
    sql = """
        INSERT INTO Gato (id_gato, esterilizado)
        VALUES (:1, :2)
    """
    cursor.execute(sql, (id_gato, esterilizado))
    print("Gato insertado correctamente.")


try:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, parametros)
            connection.commit()
            print("Insercion de datos correcta")
except oracledb.DatabaseError as error:
    print(f"no se pudo insertar el dato \n {error} \n {sql} \n {parametros} ")

def read_mascota(id:int):
    sql = (
        "SELECT * FROM MASCOTA WHERE id = :id"
    )
    parametros = {"id" : id}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
            if len(resultados) == 0:
                return print(f"no hay registros con el ID{id}")
            for fila in resultados:
                print(fila)
    except oracledb.DatabaseError as error:
        print(f"no se pudo ejecutar la query {error} \n {sql} \n {parametros}")
    

def read_perro(id:int):
    sql = (
        "SELECT * FROM PERRO WHERE id = :id"
    )
    parametros = {"id" : id}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
            if len(resultados) == 0:
                return print(f"no hay registros con el ID{id}")
            for fila in resultados:
                print(fila)
    except oracledb.DatabaseError as error:
        print(f"no se pudo ejecutar la query {error} \n {sql} \n {parametros}")

def read_ave(id:int):
    sql = (
        "SELECT * FROM AVE WHERE id = :id"
    )
    parametros = {"id" : id}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
            if len(resultados) == 0:
                return print(f"no hay registros con el ID{id}")
            for fila in resultados:
                print(fila)
    except oracledb.DatabaseError as error:
        print(f"no se pudo ejecutar la query {error} \n {sql} \n {parametros}")

def read_gato(id:int):
    sql = (
        "SELECT * FROM GATO WHERE id = :id"
    )
    parametros = {"id" : id}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
            if len(resultados) == 0:
                return print(f"no hay registros con el ID{id}")
            for fila in resultados:
                print(fila)
    except oracledb.DatabaseError as error:
        print(f"no se pudo ejecutar la query {error} \n {sql} \n {parametros}")