from flask import Flask, jsonify
import controllers
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/api/users', methods=["GET"])
@cross_origin()
def get_users():
    users = controllers.get_users()
    return jsonify(users)

app.run()