import mysql.connector


def db():
    return mysql.connector.connect(
        port="33066", user="root", password="insecure", database="briw"
    )


def close(mydb: object):
    mydb.close()


def query(mydb: object, sql: str):
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def get_data(mydb: object, table: str, limit: int = 100):
    sql = f"SELECT * FROM {table} LIMIT {limit}"
    return query(mydb, sql)
