from flask import Blueprint, jsonify, request

from ..services.patients_service import PatientsService


patients_api_bp = Blueprint('patients_api_bp', __name__)
patients_service = PatientsService()


@patients_api_bp.route('/patients', methods=['GET'])
def get_all_patients():
    patients = patients_service.get_all_patients()
    return jsonify(patients)


@patients_api_bp.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = patients_service.get_patient(patient_id)
    return jsonify(patient)


@patients_api_bp.route('/patients', methods=['POST'])
def create_patient():
    patient_data = request.json
    patient = patients_service.create_patient(patient_data)
    return jsonify(patient)


@patients_api_bp.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    patient_data = request.json
    patient = patients_service.update_patient(patient_id, patient_data)
    return jsonify(patient)


@patients_api_bp.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patients_service.delete_patient(patient_id)
    return '', 204

@patients_api_bp.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

@patients_api_bp.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400
