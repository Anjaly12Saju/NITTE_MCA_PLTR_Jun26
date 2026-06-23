import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="4smaa@pw4321",
        database="hostel_db"
    )
