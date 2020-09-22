import mysql.connector


def db(port: str, user: str, password: str, database: str):
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


def get_data(mydb: object, table: str, limit: int = 100):
    sql = f"SELECT * FROM {table} LIMIT {limit}"
    return query(mydb, sql)
