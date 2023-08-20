from flask import Flask,g
from gurukool_bp import auth_bp
from flask_session import Session
from mongo.mongo import db
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret'
app.config["SESSION_TYPE"] = "filesystem"
app.config['SESSION_FILE_THRESHOLD'] = 10
Session(app)

app.register_blueprint(auth_bp.auth_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
