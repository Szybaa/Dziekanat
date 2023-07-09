import psycopg2
from flask import Blueprint
from flask_restx import Resource, fields, Api

# Connect to the PostgreSQL database
conn = psycopg2.connect( 
    host="localhost",
      database="back",
        user="postgres",
          password="123",
            port=5432)

# Create the courses API blueprint
course_api_blueprint = Blueprint('course_api', __name__)
api = Api(course_api_blueprint, version='1.0', title='Course API', description='API for adding, deleting, and retrieving courses')

# Define course model
course_model = api.model('Course', {
    'name': fields.String(required=True, description='Course name'),
    'description': fields.String(required=True, description='Course description'),
    'id_user': fields.Integer(required=True, description='User ID')
})

class CourseResource(Resource):
    @api.expect(course_model)
    def post(self):
        # Rest of the code for adding a course
        pass

    def delete(self):
        # Rest of the code for deleting a course
        pass

    def get(self):
        # Rest of the code for retrieving courses
        pass

# Add the resource to the API
api.add_resource(CourseResource, '/add-course', '/delete-course', '/view-course')
