import json
import psycopg2
from config import host, user, password, db_name


#connect
try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
#cursor
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            #"CREATE TABLE tbl(DATE DATE DEFAULT CURRENT_DATE NOT NULL, NAME VARCHAR(20) NOT NULL, NUMBER VARCHAR(10) NOT NULL, DISTANCE VARCHAR(10) NOT NULL)"
            #"INSERT INTO tbl(DATE, NAME, NUMBER, DISTANCE) VALUES('27.02.2022', 'Petr', '1703', '1')"
            "SELECT * FROM tbl"
        )
        rows = cursor.fetchall()
        
#json
        with open("./front/src/bridge.json", "w") as file:
            json.dump(rows,file, default = str)

#renew state
    connection.commit()
    print("[INFO]Table changed sucessfully")
#if error
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
#finally
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")


