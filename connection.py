import psycopg2
def conn_to_db():

    conn = psycopg2.connect( 
        host="localhost",
        database="back",
            user="postgres",
            password="123",
                port=5432)
    
    return conn