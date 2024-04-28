from flask import Flask, request, render_template, redirect, send_file, url_for
import json

app = Flask(__name__)

# Mock database to store the last registered person
last_registered = {}

def load_questions_from_json(file_path):
    try:
        with open(file_path, 'r') as f:
            questions = json.load(f)['questions']
        return questions
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON file '{file_path}'.")
        return []

def filter_questions(questions, role, experience_level):
    filtered_questions = [
        {"question": q['question']}
        for q in questions
        if q['role'] == role and q['experience_level'] == experience_level
    ]
    return filtered_questions

def save_last_registered_to_json(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to '{file_path}'.")
    except FileNotFoundError:
        print(f"Output directory not found.")
    except PermissionError:
        print(f"Permission denied to write to '{file_path}'.")

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    # Get the form data from the request
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')
    experience_level = request.form.get('experience_level')

    # Implement basic validation of the input
    if not username or not email or not password or not role or not experience_level:
        return render_template('registration.html', error='Missing required fields')

    if len(password) < 8:
        return render_template('registration.html', error='Password must be at least 8 characters long')

    # Save the user information to the mock database
    last_registered['username'] = username
    last_registered['email'] = email
    last_registered['password'] = password
    last_registered['role'] = role
    last_registered['experience_level'] = experience_level

    # Save the user information to a JSON file
    save_last_registered_to_json(last_registered, 'last_registered.json')

    # Redirect the user to the profile page
    return redirect(url_for('user_profile'))

@app.route('/profile')
def user_profile():
    # Load questions from the JSON file (questions.json)
    questions = load_questions_from_json("questions.json")

    # Filter questions based on the user's role and experience level
    relevant_questions = filter_questions(questions, last_registered['role'], last_registered['experience_level'])

    return render_template('profile.html', user=last_registered, questions=relevant_questions)

if __name__ == '__main__':
    app.run()