import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="back",
    user="postgres",
    password="123",
    port=5432
)