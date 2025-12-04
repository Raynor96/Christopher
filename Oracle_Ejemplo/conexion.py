import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("C##christopher_ruiz")
dsn = os.getenv("10.50.1.0/xe")
password = os.getenv("inacap2025")

with oracledb.connect(
    user=username,
    password=password,
    dsn=dsn
    ) as connection:
    with connection.cursor() as cursor:
        sql = "select sysdate from dual"
        for row in cursor.execute(sql):
            for column in row:
                print(column)