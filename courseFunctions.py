import psycopg2
from connection import conn_to_db
def delete_course(course_id): 
    try:
        conn = conn_to_db()
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute the DELETE statement
        cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))

        # Commit the transaction


        return {"success": True,"msg": "Usunięto kurs pomyśnie."}

    except Exception as e:
        conn.rollback()
        return {"success": False, "msg": "Unexpected error"}

    finally:
        conn.commit()
        cursor.close()
        conn.close()

def add_course(course_name,course_description,course_id_user):
    try:
        conn = conn_to_db()
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        
        # Execute the INSERT statement
        cursor.execute(
            "INSERT INTO courses (name, description, id_user) VALUES (%s, %s, %s)",
            (course_name,course_description,course_id_user,)
        )

        # Commit the transaction
        conn.commit()

        return {"success": True,"msg": "Dodano kurs pomyśnie."}

    except Exception as e:
        return {"success": False, "msg": "Unexpected error"}

    finally:
        cursor.close()
        conn.close()