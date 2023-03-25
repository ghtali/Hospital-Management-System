from flask import Flask, jsonify, request
from typing import List
from models.lab_tests import LabTest
from services.lab_tests_service import LabTestsService

app = Flask(__name__)

lab_tests_service = LabTestsService()


@app.route('/lab_tests', methods=['POST'])
def add_lab_test():
    lab_test = LabTest(**request.json)
    added_lab_test = lab_tests_service.add_lab_test(lab_test)
    return jsonify(added_lab_test.to_dict())


@app.route('/lab_tests/<int:lab_test_id>', methods=['GET'])
def get_lab_test(lab_test_id: int):
    lab_test = lab_tests_service.get_lab_test(lab_test_id)
    if lab_test:
        return jsonify(lab_test.to_dict())
    else:
        return jsonify({'error': 'Lab test not found'}), 404


@app.route('/lab_tests/<int:lab_test_id>', methods=['PUT'])
def update_lab_test(lab_test_id: int):
    lab_test = LabTest(**request.json)
    updated_lab_test = lab_tests_service.update_lab_test(lab_test_id, lab_test)
    return jsonify(updated_lab_test.to_dict())


@app.route('/lab_tests/<int:lab_test_id>', methods=['DELETE'])
def delete_lab_test(lab_test_id: int):
    lab_tests_service.delete_lab_test(lab_test_id)
    return '', 204


@app.route('/lab_tests', methods=['GET'])
def get_all_lab_tests():
    lab_tests = lab_tests_service.get_all_lab_tests()
    lab_tests_dict = [lab_test.to_dict() for lab_test in lab_tests]
    return jsonify(lab_tests_dict)


if __name__ == '__main__':
    app.run(debug=True)
