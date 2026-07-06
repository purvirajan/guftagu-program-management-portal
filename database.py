import pandas as pd
import psycopg2

def run_query(query):
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="MukeshMakesh0920!"
    )

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

def load_sql(filename):
    with open(f"sql/{filename}", "r") as file:
        return file.read()