from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from services import doctors_service, patients_service, appointments_service, lab_tests_service, prescriptions_service

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doctors')
def get_doctors():
    return jsonify(doctors_service.get_doctors())


@app.route('/patients')
def get_patients():
    return jsonify(patients_service.get_patients())


@app.route('/appointments')
def get_appointments():
    return jsonify(appointments_service.get_appointments())


@app.route('/lab_tests')
def get_lab_tests():
    return jsonify(lab_tests_service.get_lab_tests())


@app.route('/prescriptions')
def get_prescriptions():
    return jsonify(prescriptions_service.get_prescriptions())


@app.route('/doctors', methods=['POST'])
def add_doctor():
    return jsonify(doctors_service.add_doctor(request.json))


@app.route('/patients', methods=['POST'])
def add_patient():
    return jsonify(patients_service.add_patient(request.json))


@app.route('/appointments', methods=['POST'])
def add_appointment():
    return jsonify(appointments_service.add_appointment(request.json))


@app.route('/lab_tests', methods=['POST'])
def add_lab_test():
    return jsonify(lab_tests_service.add_lab_test(request.json))


@app.route('/prescriptions', methods=['POST'])
def add_prescription():
    return jsonify(prescriptions_service.add_prescription(request.json))


@app.route('/doctors/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    return jsonify(doctors_service.update_doctor(doctor_id, request.json))


@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    return jsonify(patients_service.update_patient(patient_id, request.json))


@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    return jsonify(appointments_service.update_appointment(appointment_id, request.json))


@app.route('/lab_tests/<int:lab_test_id>', methods=['PUT'])
def update_lab_test(lab_test_id):
    return jsonify(lab_tests_service.update_lab_test(lab_test_id, request.json))


@app.route('/prescriptions/<int:prescription_id>', methods=['PUT'])
def update_prescription(prescription_id):
    return jsonify(prescriptions_service.update_prescription(prescription_id, request.json))


@app.route('/doctors/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    return jsonify(doctors_service.delete_doctor(doctor_id))


@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    return jsonify(patients_service.delete_patient(patient_id))


@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    return jsonify(appointments_service.delete_appointment(appointment_id))


@app.route('/lab_tests/<int:lab_test_id>', methods=['DELETE'])
def delete_lab_test(lab_test_id):
    return jsonify(lab_tests_service.delete_lab_test(lab_test_id))


@app.route('/prescriptions/<int:prescription_id>', methods=['DELETE'])
def delete_prescription(prescription_id):
    return jsonify(prescriptions_service.delete_prescription(prescription_id))


if __name__ == '__main__':
    app.run(debug=True)
