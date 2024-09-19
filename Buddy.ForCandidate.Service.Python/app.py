from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from llm_client import get_gpt_response
from utils import clean_markdown
import uuid
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_details_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class UserDetails(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    current_position = db.Column(db.String(100), nullable=False)
    looking_for_position = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'current_position': self.current_position,
            'looking_for_position': self.looking_for_position,
            'skills': self.skills,
            'phone_number': self.phone_number
        }

def initialize_database():
    with app.app_context():
        db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user-details', methods=['POST'])
def add_user_details():
    user_details = request.get_json()
    app.logger.debug(f"Received JSON payload: {user_details}")
    
    if not user_details:
        return jsonify({'error': 'Invalid JSON payload'}), 400
    
    required_fields = ['first_name', 'last_name', 'current_position', 'looking_for_position', 'skills', 'phone_number']
    
    for field in required_fields:
        if field not in user_details:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    new_user = UserDetails(
        first_name=user_details['first_name'],
        last_name=user_details['last_name'],
        current_position=user_details['current_position'],
        looking_for_position=user_details['looking_for_position'],
        skills=user_details['skills'],
        phone_number=user_details['phone_number']
    )
    db.session.add(new_user)
    db.session.commit()
    app.logger.debug(f"Added new user: {new_user}")
    return jsonify({'message': 'User details added successfully!', 'id': new_user.id}), 201

@app.route('/user-details/<id>', methods=['GET'])
def get_user_details(id):
    app.logger.debug(f"Fetching user details for ID: {id}")
    user_details = db.session.get(UserDetails, id)
    if user_details is None:
        return jsonify({'error': 'User not found'}), 404
    return user_details.to_dict()

@app.route('/user_resume/<id>', methods=['GET'])
def get_user_resume(id):
    return get_gpt_response_for_user(id, "Please send me resume", "Resume")

@app.route('/linked_in_profile/<id>', methods=['GET'])
def get_user_linked_in_profile(id):
    return get_gpt_response_for_user(id, "Can you please send me suggestions for open linked in profile", "Linked in profile")

@app.route('/leet_code_exercises/<id>', methods=['GET'])
def get_leet_code_exercises(id):
    return get_gpt_response_for_user(id, "Please send me leet code exercises according to my profile", "Leet code exercises")

@app.route('/mock_interview/<id>', methods=['GET'])
def get_mock_interview(id):
    return get_gpt_response_for_user(id, "Can you please demonstrate me mock interview", "Mock interview")

@app.route('/salary_negotiation/<id>', methods=['GET'])
def get_salary_negotiation(id):
    return get_gpt_response_for_user(id, "Can you please send me salary negotiation", "Salary negotiation")

def get_gpt_response_for_user(id, prompt, message_to_log):
    app.logger.debug(f"{message_to_log} for user ID: {id}")
    user_details = db.session.get(UserDetails, id)
    if user_details is None:
        return jsonify({'error': 'User not found'}), 404
    gpt_response = get_gpt_response(f"{prompt} for: {user_details.to_dict()}", 'dev-gpt-4o-2024-08-06-chat-completions')
    response = clean_markdown(gpt_response)
    return response

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)