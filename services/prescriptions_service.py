from flask import Flask, jsonify, request
from typing import List
from models.prescriptions import Prescription
from services.prescriptions_service import PrescriptionsService

app = Flask(__name__)

prescriptions_service = PrescriptionsService()


@app.route('/prescriptions', methods=['POST'])
def add_prescription():
    prescription = Prescription(**request.json)
    added_prescription = prescriptions_service.add_prescription(prescription)
    return jsonify(added_prescription.to_dict())


@app.route('/prescriptions/<int:prescription_id>', methods=['GET'])
def get_prescription(prescription_id: int):
    prescription = prescriptions_service.get_prescription(prescription_id)
    if prescription:
        return jsonify(prescription.to_dict())
    else:
        return jsonify({'error': 'Prescription not found'}), 404


@app.route('/prescriptions/<int:prescription_id>', methods=['PUT'])
def update_prescription(prescription_id: int):
    prescription = Prescription(**request.json)
    updated_prescription = prescriptions_service.update_prescription(
        prescription_id, prescription)
    return jsonify(updated_prescription.to_dict())


@app.route('/prescriptions/<int:prescription_id>', methods=['DELETE'])
def delete_prescription(prescription_id: int):
    prescriptions_service.delete_prescription(prescription_id)
    return '', 204


@app.route('/prescriptions', methods=['GET'])
def get_all_prescriptions():
    prescriptions = prescriptions_service.get_all_prescriptions()
    prescriptions_dict = [prescription.to_dict()
                          for prescription in prescriptions]
    return jsonify(prescriptions_dict)


if __name__ == '__main__':
    app.run(debug=True)
