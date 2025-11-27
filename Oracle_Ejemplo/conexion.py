import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
dsn = os.getenv("ORACLE_DSN")

def get_connection():
    try:
        return oracledb.connect(
            user=username,
            password=password,
            dsn=dsn
        )
    except oracledb.DatabaseError as error:
        print("Error al conectar a Oracle:", error)
        return None

def create_schema_all():
    tables = [

        
        (
            "CREATE TABLE Mascota ("
            "id_mascota NUMBER PRIMARY KEY, "
            "edad NUMBER, "
            "especie VARCHAR2(255), "
            "historialMedico VARCHAR2(255)"
            ")"
        ),

        # Tabla Perro
        (
            "CREATE TABLE Perro ("
            "id_mascota NUMBER PRIMARY KEY, "
            "historialVacunas VARCHAR2(255), "
            "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota) ON DELETE CASCADE"
            ")"
        ),

        # Tabla Ave
        (
            "CREATE TABLE Ave ("
            "id_mascota NUMBER PRIMARY KEY, "
            "tipoJaula VARCHAR2(255), "
            "controlVuelo CHAR(1) CHECK (controlVuelo IN ('S','N')), "
            "FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota) ON DELETE CASCADE"
            ")"
        ),

        # Tabla Gato
        (
            "CREATE TABLE Gato ("
            "id_gato NUMBER PRIMARY KEY, "
            "esterilizado CHAR(1) CHECK (esterilizado IN ('S','N')), "
            "CONSTRAINT fk_gato_mascota "
            "FOREIGN KEY (id_gato) REFERENCES Mascota(id_mascota) ON DELETE CASCADE"
            ")"
        ),
    ]


    for query in tables:
        create_schema(query)

create_schema_all()

#Insertar datos

def insertar_mascota(connection, id_mascota, edad, especie, historialMedico):
    sql = """
        INSERT INTO Mascota (id_mascota, edad, especie, historialMedico)
        VALUES (:1, :2, :3, :4)
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (id_mascota, edad, especie, historialMedico))
            connection.commit()
            print("Mascota insertada correctamente.")

    except Exception as e:
        print("Error insertando mascota:", e)



 
def insertar_perro(connection, id_mascota, historialVacunas):
    sql = """
        INSERT INTO Perro (id_mascota, historialVacunas)
        VALUES (:1, :2)
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (id_mascota, historialVacunas))
            connection.commit()
            print("Perro insertado correctamente.")

    except Exception as e:
        print("Error insertando perro:", e)



def insertar_ave(connection, id_mascota, tipoJaula, controlVuelo):
    sql = """
        INSERT INTO Ave (id_mascota, tipoJaula, controlVuelo)
        VALUES (:1, :2, :3)
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (id_mascota, tipoJaula, controlVuelo))
            connection.commit()
            print("Ave insertada correctamente.")

    except Exception as e:
        print("Error insertando ave:", e)




def insertar_gato(connection, id_gato, esterilizado):
    sql = """
        INSERT INTO Gato (id_gato, esterilizado)
        VALUES (:1, :2)
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (id_gato, esterilizado))
            connection.commit()
            print("Gato insertado correctamente.")

    except Exception as e:
        print("Error insertando gato:", e)



try:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")
except oracledb.DatabaseError as error:
    print(f"No se pudo insertar el dato:\n{error}\nSQL: {sql}\nParámetros: {parametros}")


import oracledb
from connection import get_connection

def read_mascota(id_mascota: int):
    sql = "SELECT id_mascota, edad, especie, historialMedico FROM Mascota WHERE id_mascota = :id"
    parametros = {"id": id_mascota}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                row = cursor.fetchone()

                if row is None:
                    print(f"No hay registros con el ID {id_mascota}")
                    return None

                mascota = {
                    "id_mascota": row[0],
                    "edad": row[1],
                    "especie": row[2],
                    "historialMedico": row[3]
                }

                print("Mascota encontrada:")
                print(mascota)
                return mascota

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query:\n{error}\nSQL: {sql}\nParámetros: {parametros}")
        return None

    

import oracledb
from connection import get_connection

def read_perro(id_mascota: int):
    sql = "SELECT id_mascota, historialVacunas FROM Perro WHERE id_mascota = :id"
    parametros = {"id": id_mascota}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                row = cursor.fetchone()

                if row is None:
                    print(f"No existe un Perro con el ID {id_mascota}")
                    return None

                perro = {
                    "id_mascota": row[0],
                    "historialVacunas": row[1]
                }

                print("Perro encontrado:")
                print(perro)
                return perro

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query:\n{error}\nSQL: {sql}\nParámetros: {parametros}")
        return None


import oracledb
from connection import get_connection

def read_ave(id_mascota: int):
    sql = """
        SELECT id_mascota, tipoJaula, controlVuelo
        FROM Ave
        WHERE id_mascota = :id
    """

    parametros = {"id": id_mascota}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                row = cursor.fetchone()

                if row is None:
                    print(f"No existe un Ave con el ID {id_mascota}")
                    return None

                ave = {
                    "id_mascota": row[0],
                    "tipoJaula": row[1],
                    "controlVuelo": row[2]
                }

                print("✔ Ave encontrada:")
                print(ave)
                return ave

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query:\n{error}\nSQL: {sql}\nParámetros: {parametros}")
        return None


import oracledb
from connection import get_connection

def read_gato(id_gato: int):
    sql = """
        SELECT id_gato, esterilizado
        FROM Gato
        WHERE id_gato = :id
    """

    parametros = {"id": id_gato}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                row = cursor.fetchone()

                if row is None:
                    print(f"No existe un Gato con el ID {id_gato}")
                    return None

                gato = {
                    "id_gato": row[0],
                    "esterilizado": row[1]
                }

                print("✔ Gato encontrado:")
                print(gato)
                return gato

    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query:\n{error}\nSQL: {sql}\nParámetros: {parametros}")
        return None




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
   
    def update_perro(
    id_mascota: int,
    edad: Optional[int] = None,
    especie: Optional[str] = None,
    historial_vacuna: Optional[str] = None
):
    
   def update_mascota(id_mascota, edad=None, especie=None, historialMedico=None):
    modificaciones = []
    parametros = {"id_mascota": id_mascota}

    if edad is not None:
        modificaciones.append("edad = :edad")
        parametros["edad"] = edad

    if especie is not None:
        modificaciones.append("especie = :especie")
        parametros["especie"] = especie

    if historialMedico is not None:
        modificaciones.append("historialMedico = :historialMedico")
        parametros["historialMedico"] = historialMedico

    if not modificaciones:
        return
    
    sql = f"UPDATE Mascota SET {', '.join(modificaciones)} WHERE id_mascota = :id_mascota"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            conn.commit()



def update_ave(
    id_mascota: int,
    tipo_jaula: Optional[str] = None, 
    control_vuelo: Optional[str] = None, 
    historial_medico: Optional[str] = None
):
    
    if historial_medico is not None:
        update_mascota(id_mascota, historialMedico=historial_medico)

    modificaciones = []
    parametros = {"id_mascota": id_mascota}

    if tipo_jaula is not None:
        modificaciones.append("tipoJaula = :tipo_jaula")
        parametros["tipo_jaula"] = tipo_jaula

    if control_vuelo is not None:
        modificaciones.append("controlVuelo = :control_vuelo")
        parametros["control_vuelo"] = control_vuelo

    if not modificaciones:
        print("No se proporcionaron datos de Ave para actualizar.")
        return

    sql = f"UPDATE Ave SET {', '.join(modificaciones)} WHERE id_mascota = :id_mascota"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            conn.commit()
            print(f"✔ Ave con ID {id_mascota} actualizada correctamente.")

            
#Editar persona

def update_gato(
    id_gato: int,
    esterilizado: Optional[str] = None,
    historial_medico: Optional[str] = None
):
    
    if historial_medico is not None:
        update_mascota(id_gato, historialMedico=historial_medico)

    modificaciones = []
    parametros = {"id_gato": id_gato}

    if esterilizado is not None:
        modificaciones.append("esterilizado = :esterilizado")
        parametros["esterilizado"] = esterilizado

    if not modificaciones:
        print("No se proporcionaron datos de Gato para actualizar.")
        return

    sql = f"UPDATE Gato SET {', '.join(modificaciones)} WHERE id_gato = :id_gato"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
            conn.commit()
            print(f"✔ Gato con ID {id_gato} actualizado correctamente.")


#eliminacion de datos

def delete_mascota(id_mascota: int):
    sql = "DELETE FROM Mascota WHERE id_mascota = :id"
    parametros = {"id": id_mascota}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
                conn.commit()

                if cur.rowcount == 0:
                    print(f"No existe Mascota con ID {id_mascota}")
                else:
                    print(f"Mascota con ID {id_mascota} eliminada correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al eliminar:\n{e}\nSQL: {sql}\nParámetros: {parametros}")


def delete_perro(id_mascota: int):
    sql = "DELETE FROM Perro WHERE id_mascota = :id"
    parametros = {"id": id_mascota}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
                conn.commit()

                if cur.rowcount == 0:
                    print(f"No existe Perro con ID {id_mascota}")
                else:
                    print(f"Perro con ID {id_mascota} eliminado correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al eliminar:\n{e}\nSQL: {sql}\nParámetros: {parametros}")



def delete_gato(id_gato: int):
    sql = "DELETE FROM Gato WHERE id_gato = :id"
    parametros = {"id": id_gato}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
                conn.commit()

                if cur.rowcount == 0:
                    print(f"No existe Gato con ID {id_gato}")
                else:
                    print(f"Gato con ID {id_gato} eliminado correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al eliminar:\n{e}\nSQL: {sql}\nParámetros: {parametros}")


def delete_ave(id_mascota: int):
    sql = "DELETE FROM Ave WHERE id_mascota = :id"
    parametros = {"id": id_mascota}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
                conn.commit()

                if cur.rowcount == 0:
                    print(f"No existe Ave con ID {id_mascota}")
                else:
                    print(f"Ave con ID {id_mascota} eliminada correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al eliminar:\n{e}\nSQL: {sql}\nParámetros: {parametros}")


 





