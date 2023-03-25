from flask import Flask, jsonify, request
from typing import List
from models.patients import Patient
from services.patients_service import PatientsService

app = Flask(__name__)

patients_service = PatientsService()


@app.route('/patients', methods=['POST'])
def add_patient():
    patient = Patient(**request.json)
    added_patient = patients_service.add_patient(patient)
    return jsonify(added_patient.to_dict())


@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id: int):
    patient = patients_service.get_patient(patient_id)
    if patient:
        return jsonify(patient.to_dict())
    else:
        return jsonify({'error': 'Patient not found'}), 404


@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id: int):
    patient = Patient(**request.json)
    updated_patient = patients_service.update_patient(patient_id, patient)
    return jsonify(updated_patient.to_dict())


@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id: int):
    patients_service.delete_patient(patient_id)
    return '', 204


@app.route('/patients', methods=['GET'])
def get_all_patients():
    patients = patients_service.get_all_patients()
    patients_dict = [patient.to_dict() for patient in patients]
    return jsonify(patients_dict)


if __name__ == '__main__':
    app.run(debug=True)
