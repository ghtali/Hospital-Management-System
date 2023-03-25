from flask import Flask, jsonify, request
from typing import List
from models.appointments import Appointment
from services.appointments_service import AppointmentsService


app = Flask(__name__)

appointments_service = AppointmentsService()


@app.route('/appointments', methods=['POST'])
def add_appointment():
    appointment = Appointment(**request.json)
    added_appointment = appointments_service.add_appointment(appointment)
    return jsonify(added_appointment.to_dict())


@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id: int):
    appointment = appointments_service.get_appointment(appointment_id)
    if appointment:
        return jsonify(appointment.to_dict())
    else:
        return jsonify({'error': 'Appointment not found'}), 404


@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id: int):
    appointment = Appointment(**request.json)
    updated_appointment = appointments_service.update_appointment(
        appointment_id, appointment)
    return jsonify(updated_appointment.to_dict())


@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id: int):
    appointments_service.delete_appointment(appointment_id)
    return '', 204


@app.route('/appointments', methods=['GET'])
def get_all_appointments():
    appointments = appointments_service.get_all_appointments()
    appointments_dict = [appointment.to_dict() for appointment in appointments]
    return jsonify(appointments_dict)


if __name__ == '__main__':
    app.run(debug=True)
