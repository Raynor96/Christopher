import oracledb
import os
from dotenv import load_dotenv

load_dotenv()


username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

class Auth:
    @staticmethod
    def register():
        pass
    @staticmethod
    def login():
        pass

"""
Unidad de Fomento (UF).
Índice de valor Promedio (IVP).
Índice de Precio al Consumidor (IPC).
Unidad Tributaria Mensual (UTM).
Dólar -> CLP.
Euro -> CLP.

"""

class Finance:
    @staticmethod
    def get_uf():
        pass
    @staticmethod
    def get_vip():
        pass
    @staticmethod
    def get_ipc():
        pass
    @staticmethod
    def get_utm():
        pass
    @staticmethod
    def get_usd():
        pass
    @staticmethod
    def get_eur():
        pass

class Datebase:
    def __init__(self, username,password,dsn):
        self.username = username
        self.password = password
        self.dsn = dsn
    def getconnection(self):
        return oracledb.connect(user=self.username, password=self.password, dsn=self.dsn)