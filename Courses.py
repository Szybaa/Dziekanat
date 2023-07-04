import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="back",
    user="postgres",
    password="123",
    port=5432
)

def add_course(course_name, course_description, user_id):
    try:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO courses (name, description, id_user) VALUES (%s, %s, %s)",
            (course_name, course_description, user_id)
        )

        conn.commit()

        print("Course added successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error adding course:", error)

    finally:
        cursor.close()

def delete_course(course_id):
    try:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))

        conn.commit()

        print("Course deleted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error deleting course:", error)

    finally:
        cursor.close()

add_course("test", "test", 1)
#delete_course(1)