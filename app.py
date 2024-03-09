from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.get_json()

    if 'name' not in data:
        return jsonify({'error': 'Name is missing'}), 400

    name = data['name']
    greeting = f'Hello, {name}!'
    return jsonify({'greeting': greeting})

@app.route("/welcome")
def welcome():
    return "welcome"

if __name__ == '__main__':
    app.run(debug=True)
