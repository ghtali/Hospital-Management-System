from flask import Blueprint, jsonify

from ..services import doctors_service

doctors_api_bp = Blueprint('doctors_api', __name__, url_prefix='/api/doctors')


@doctors_api_bp.route('', methods=['GET'])
def get_doctors():
    doctors = doctors_service.get_all_doctors()
    return jsonify(doctors)


@doctors_api_bp.route('/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = doctors_service.get_doctor_by_id(doctor_id)
    if doctor:
        return jsonify(doctor)
    return jsonify({'message': 'Doctor not found'}), 404


@doctors_api_bp.route('', methods=['POST'])
def create_doctor():
    request_data = request.get_json()
    new_doctor = doctors_service.create_doctor(request_data)
    return jsonify(new_doctor), 201


@doctors_api_bp.route('/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    request_data = request.get_json()
    updated_doctor = doctors_service.update_doctor(doctor_id, request_data)
    if updated_doctor:
        return jsonify(updated_doctor)
    return jsonify({'message': 'Doctor not found'}), 404


@doctors_api_bp.route('/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    success = doctors_service.delete_doctor(doctor_id)
    if success:
        return '', 204
    return jsonify({'message': 'Doctor not found'}), 404
