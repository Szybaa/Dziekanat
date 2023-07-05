from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
     host="localhost",
       database="back",
         user="postgres",
           password="123",
             port=5432)

# Create Flask app
app = Flask(__name__)
CORS(app)

# Create Flask-RestX API
api = Api(app, version='1.0', title='Course API', description='API for adding, deleting, and retrieving courses')

# Define course model
course_model = api.model('Course', {
    'name': fields.String(required=True, description='Course name'),
    'description': fields.String(required=True, description='Course description'),
    'id_user': fields.Integer(required=True, description='User ID')
})

class CourseResource(Resource):
    @api.expect(course_model)
    def post(self):
        course_data = api.payload

        try:
            # Create a cursor object to interact with the database
            cursor = conn.cursor()

            # Execute the INSERT statement
            cursor.execute(
                "INSERT INTO courses (name, description, id_user) VALUES (%s, %s, %s)",
                (course_data['name'], course_data['description'], course_data['id_user'])
            )

            # Commit the transaction
            conn.commit()

            return {'message': 'Course added successfully'}, 201

        except (Exception, psycopg2.Error) as error:
            return {'message': 'Error adding course: {}'.format(error)}, 500

        finally:
            # Close the cursor
            cursor.close()

    @api.param('course_id', 'Course ID', type='integer', required=True)
    def delete(self, course_id):
        try:
            # Create a cursor object to interact with the database
            cursor = conn.cursor()

            # Execute the DELETE statement
            cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))

            # Commit the transaction
            conn.commit()

            return {'message': 'Course deleted successfully'}, 200

        except (Exception, psycopg2.Error) as error:
            return {'message': 'Error deleting course: {}'.format(error)}, 500

        finally:
            # Close the cursor
            cursor.close()

    def get(self):
        try:
            # Create a cursor object to interact with the database
            cursor = conn.cursor()

            # Execute the SELECT statement to retrieve all courses
            cursor.execute("SELECT * FROM courses")

            # Fetch all rows from the cursor
            rows = cursor.fetchall()

            # Transform rows into a list of dictionaries
            courses = []
            for row in rows:
                course = {
                    'id': row[0],
                    'name': row[1],
                    'description': row[2],
                    'id_user': row[3]
                }
                courses.append(course)

            return {'courses': courses}, 200

        except (Exception, psycopg2.Error) as error:
            return {'message': 'Error retrieving courses: {}'.format(error)}, 500

        finally:
            # Close the cursor
            cursor.close()

# Add resource to the API
api.add_resource(CourseResource, '/courses')

if __name__ == '__main__':
    app.run()