from flask import Blueprint, jsonify, request

from ..services.prescriptions_service import PrescriptionsService

prescriptions_api_bp = Blueprint('prescriptions_api', __name__)
prescriptions_service = PrescriptionsService()


@prescriptions_api_bp.route('/prescriptions', methods=['POST'])
def create_prescription():
    data = request.json
    prescription = prescriptions_service.create_prescription(data)
    return jsonify(prescription), 201


@prescriptions_api_bp.route('/prescriptions/<int:prescription_id>', methods=['GET'])
def get_prescription(prescription_id):
    prescription = prescriptions_service.get_prescription(prescription_id)
    if prescription:
        return jsonify(prescription), 200
    else:
        return jsonify({'error': 'Prescription not found'}), 404


@prescriptions_api_bp.route('/prescriptions/<int:prescription_id>', methods=['PUT'])
def update_prescription(prescription_id):
    data = request.json
    prescription = prescriptions_service.update_prescription(
        prescription_id, data)
    if prescription:
        return jsonify(prescription), 200
    else:
        return jsonify({'error': 'Prescription not found'}), 404


@prescriptions_api_bp.route('/prescriptions/<int:prescription_id>', methods=['DELETE'])
def delete_prescription(prescription_id):
    success = prescriptions_service.delete_prescription(prescription_id)
    if success:
        return '', 204
    else:
        return jsonify({'error': 'Prescription not found'}), 404


@prescriptions_api_bp.route('/prescriptions', methods=['GET'])
def get_prescriptions():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    prescriptions = prescriptions_service.get_prescriptions(
        start_date, end_date)
    return jsonify(prescriptions), 200
