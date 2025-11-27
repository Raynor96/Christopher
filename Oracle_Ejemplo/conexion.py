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



from typing import Optional

from typing import Optional 
from datetime import datetime 


def get_connection():
   
    class MockCursor:
        def execute(self, sql, params):
            print(f"Ejecutando SQL: {sql} con parámetros: {params}")
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_val, exc_tb): pass

    class MockConnection:
        def cursor(self): return MockCursor()
        def commit(self): print("Transacción confirmada.")
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_val, exc_tb): pass

    return MockConnection()

def update_mascota(
    id_mascota: int,
    edad: Optional[int] = None,
    especie: Optional[str] = None,
    historial_medico: Optional[str] = None 
):
    modificaciones = []
   
    parametros = {"id_mascota": id_mascota}

    if edad is not None:
       
        modificaciones.append("edad = :edad")
        parametros["edad"] = edad

    if especie is not None:
        modificaciones.append("especie = :especie")
        parametros["especie"] = especie

    if historial_medico is not None:
        
        modificaciones.append("HistorialMedico = :historial_medico")
        
        parametros["historial_medico"] = historial_medico

    if not modificaciones:
        
        print("No has enviado datos por modificar para la mascota.")
        return

   
    sql = f"UPDATE mascota SET {", ".join(modificaciones)} WHERE id_mascota = :id_mascota"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            conn.commit()
          
            print(f"Dato con ID = {id_mascota} actualizado en tabla 'mascota'")



def update_perro(
    id_mascota: int,
    edad: Optional[int] = None,
    especie: Optional[str] = None,
    historial_vacuna: Optional[str] = None 
):
   
    update_mascota(id_mascota, edad, especie)
    
   
    modificaciones = []
    parametros = {"id_mascota": id_mascota} 

    if historial_vacuna is not None:
       
        modificaciones.append("HistorialVacuna = :historial_vacuna")
        
        parametros["historial_vacuna"] = historial_vacuna
        
    if not modificaciones:
       
        return 

    
    sql = f"UPDATE perro SET {", ".join(modificaciones)} WHERE id_mascota = :id_mascota"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID = {id_mascota} actualizado en tabla 'perro'")


def update_ave( 
    id_mascota: int,
    tipo_jaula: Optional[int] = None, # 
    control_vuelo: Optional[str] = None, # 
    historial_medico: Optional[str] = None # 
):
    
    if historial_medico is not None:
        update_mascota(id_mascota, historial_medico=historial_medico)

    modificaciones = []
    
    parametros = {"id_mascota": id_mascota}

   
    if tipo_jaula is not None:
        modificaciones.append("TipoJaula = :tipo_jaula")
        parametros["tipo_jaula"] = tipo_jaula

    
    if control_vuelo is not None:
        modificaciones.append("controlVuelo = :control_vuelo")
        parametros["control_vuelo"] = control_vuelo

    if not modificaciones:
        print("No has enviado datos específicos de Ave por modificar.")
        return

    
    sql = f"UPDATE ave SET {", ".join(modificaciones)} WHERE id_mascota = :id_mascota"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID = {id_mascota} actualizado en tabla 'ave'")
            


def update_gato(
    id_mascota: int, 
    esterilizado: Optional[int] = None,
    historial_medico: Optional[str] = None 
):
    
    if historial_medico is not None:
        update_mascota(id_mascota, historial_medico=historial_medico)
        
    modificaciones = []
    
    parametros = {"id_mascota": id_mascota}

    if esterilizado is not None:
        modificaciones.append("esterilizado = :esterilizado")
        parametros["esterilizado"] = esterilizado

    if not modificaciones:
        print("No has enviado datos específicos de Gato por modificar.")
        return

    
    sql = f"UPDATE gato SET {", ".join(modificaciones)} WHERE id_mascota = :id_mascota"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato con ID = {id_mascota} actualizado en tabla 'gato'")

#eliminacion de datos

def delete_mascota(id_mascota: int):
    sql = (
        "DELETE FROM MASCOTA WHERE id = :id"
    )
    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor()as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado /n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} /n {sql} /n {parametros}")

def delete_perro(id: int):
    sql