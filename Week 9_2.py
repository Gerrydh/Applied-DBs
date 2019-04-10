import pymysql

conn - None

def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="school", cursorclass=pymysql.cursors.DictCursor )

def get_experience(number):
    if (not conn):
        connect();
    query = "select * from teacher where experience < %s"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query, (number)) 
        x = cursor.fetchall()
        return x
