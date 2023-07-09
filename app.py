from flask import Flask
from flask_cors import CORS
from Courses import course_api_blueprint

app = Flask(__name__)
CORS(app)

# Register the courses API blueprint
app.register_blueprint(course_api_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run()
