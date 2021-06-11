from flask import Flask, jsonify
import controllers

app = Flask(__name__)

@app.route('/users', methods=["GET"])
def get_users():
    users = controllers.get_users()
    return jsonify(users)

app.run()