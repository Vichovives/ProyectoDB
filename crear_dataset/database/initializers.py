# Conexion a DB
import psycopg2

def DBInstance():
    try:
        conn = psycopg2.connect(
            host="db-postgresql-nyc3-82326-do-user-14766642-0.c.db.ondigitalocean.com",
            database="defaultdb",
            user="doadmin",
            password="AVNS_GjSOTWxWLvet9bAlVOL",
            port=25060
        )
        return conn
    except psycopg2.Error as err:
        print("Error al conectar la base de datos: ", err)
        return None