import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()


def db(database: str):
    port = os.environ.get("mysql_port")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    try:
        return mysql.connector.connect(
            port=port, user=user, password=password, database=database
        )
    except:
        print("DB Error")


def close(mydb: object):
    mydb.close()


def query(mydb: object, sql: str):
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def update(mydb: object, sql: str, data: any):
    try:
        cursor = mydb.cursor()
        cursor.execute(sql, data)
        mydb.commit()
    except:
        print("Failed to update db")


def update_with_dict(mydb: object, table:str, data: dict):

    f = ", ".join(data.keys())
    vals = ""
    for i in range(0, len(data.keys())):
        vals += "%s, "

    sql = f"INSERT INTO {table} ({f}) VALUES({vals.strip(', ')})"

    update(sql, data.values())


def get_data(mydb: object, table: str, limit: int = 100):
    sql = f"SELECT * FROM {table} LIMIT {limit}"
    return query(mydb, sql)
