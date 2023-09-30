import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from ..db.repositories import UserRepository
from ..db.models import User

from ..db import init_app, db

from ..db.interfaces import PatientRepositoryInterface


app = Flask(__name__)

CORS(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user_repo = UserRepository(session)
    return user_repo.get_user_by_id(user_id)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///default.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_app(app)
db.create_all()


@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(PatientRepositoryInterface.get_patients())


@app.route('/patients', methods=['POST'])
def add_patient():
    return jsonify(PatientRepositoryInterface.add_patient(request.get_json()))


@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    return jsonify(PatientRepositoryInterface.get_patient(patient_id))


@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    return jsonify(PatientRepositoryInterface.update_patient(patient_id, request.get_json()))


@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    return jsonify(PatientRepositoryInterface.delete_patient(patient_id))


if __name__ == '__main__':
    app.run()

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": str(error)}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        session = Session()
        user_repo = UserRepository(session)
        user = user_repo.get_user_by_username(username)
        if user and check_password_hash(user.hashed_password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
