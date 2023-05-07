from flask import Flask, jsonify, request
from flask_cors import CORS
from db import init_app, db

from db.interfaces import PatientRepositoryInterface


app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hospuser:qaz123ZAQ@localhost/hospital'
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
