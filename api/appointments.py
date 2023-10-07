
from flask import Blueprint, jsonify, request

from ..services.appointments_service import AppointmentsService

appointments_api_bp = Blueprint('appointments_api', __name__)
appointments_service = AppointmentsService()

# Define Flask routes based on the original FastAPI routes...

# TODO: Define the necessary routes here


@appointments_api_bp.route('/appointments', methods=['GET'])
def get_all_appointments():
    appointments = appointments_service.get_all_appointments()
    return jsonify(appointments)

@appointments_api_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = appointments_service.get_appointment_by_id(appointment_id)
    if appointment:
        return jsonify(appointment)
    return jsonify({"error": "Appointment not found"}), 404

