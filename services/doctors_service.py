from flask import Flask, jsonify, request
from typing import List
from models.doctors import Doctor
from services.doctors_service import DoctorsService


app = Flask(__name__)

doctors_service = DoctorsService()


@app.route('/doctors', methods=['POST'])
def add_doctor():
    doctor = Doctor(**request.json)
    added_doctor = doctors_service.add_doctor(doctor)
    return jsonify(added_doctor.to_dict())


@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id: int):
    doctor = doctors_service.get_doctor(doctor_id)
    if doctor:
        return jsonify(doctor.to_dict())
    else:
        return jsonify({'error': 'Doctor not found'}), 404


@app.route('/doctors/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id: int):
    doctor = Doctor(**request.json)
    updated_doctor = doctors_service.update_doctor(doctor_id, doctor)
    return jsonify(updated_doctor.to_dict())


@app.route('/doctors/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id: int):
    doctors_service.delete_doctor(doctor_id)
    return '', 204


@app.route('/doctors', methods=['GET'])
def get_all_doctors():
    doctors = doctors_service.get_all_doctors()
    doctors_dict = [doctor.to_dict() for doctor in doctors]
    return jsonify(doctors_dict)


if __name__ == '__main__':
    app.run(debug=True)
