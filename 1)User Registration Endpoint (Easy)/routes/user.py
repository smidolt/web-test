from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

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

    user = {
        'username': username,
        'email': email,
        'password': password
    }

    return render_template('success.html', user=user)

if __name__ == '__main__':
    app.run()