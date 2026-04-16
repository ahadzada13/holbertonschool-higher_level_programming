#!/usr/bin/python3
"""
Simple API development using the Flask framework.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# User-ləri yaddaşda saxlamaq üçün lüğət
users = {}


@app.route("/")
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Handles POST requests to add a new user."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        # 409 Conflict status kodu təkrarlanan data üçün vacibdir
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
