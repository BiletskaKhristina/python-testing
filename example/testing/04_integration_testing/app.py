from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Application is working"})


@app.route("/users")
def get_users():
    users = [
        {"id": 1, "name": "Anna"},
        {"id": 2, "name": "Oleh"},
    ]
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)