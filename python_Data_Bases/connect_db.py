import mysql.connector
from mysql.connector import Error
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    """Conecta a la base de datos MySQL y devuelve la conexión."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def insert_data_to_db(df, table_name):
    """Inserta los datos de un DataFrame en una tabla MySQL."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cols = ", ".join(df.columns)
            placeholders = ", ".join(["%s"] * len(df.columns))
            sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            data = df.values.tolist()
            cursor.executemany(sql, data)
            connection.commit()
            print("Datos insertados correctamente.")
        except Error as e:
            print(f"Error al insertar datos en la base de datos: {e}")
        finally:
            cursor.close()
            connection.close()