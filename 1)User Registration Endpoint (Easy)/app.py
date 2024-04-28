from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

last_registered = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    last_registered['username'] = username
    last_registered['email'] = email
    last_registered['password'] = password

    return jsonify({'message': 'User registered successfully', 'redirect': '/last_registered'}), 200

@app.route('/last_registered')
def last_registered_person():
    return render_template('last_registered.html', user=last_registered)

if __name__ == '__main__':
    app.run()