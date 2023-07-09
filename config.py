from flask_restx import reqparse

# Parser for the course ID
course_id_parser = reqparse.RequestParser()
course_id_parser.add_argument('course_id', type=int, required=True, help='Course ID is required')
