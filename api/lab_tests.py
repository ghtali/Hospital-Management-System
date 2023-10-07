from flask import Blueprint, jsonify, request

from ..services.lab_tests_service import LabTestsService


lab_tests_api_bp = Blueprint('lab_tests_api', __name__)
lab_tests_service = LabTestsService()


@lab_tests_api_bp.route('/lab_tests', methods=['POST'])
def create_lab_test():
    data = request.json
    lab_test = lab_tests_service.add_lab_test(data)
    return jsonify(lab_test), 201


@lab_tests_api_bp.route('/lab_tests', methods=['GET'])
def get_all_lab_tests():
    lab_tests = lab_tests_service.get_all_lab_tests()
    return jsonify(lab_tests)


@lab_tests_api_bp.route('/lab_tests/<int:lab_test_id>', methods=['GET'])
def get_lab_test(lab_test_id):
    # TODO: Implement get_lab_test endpoint
    pass


@lab_tests_api_bp.route('/lab_tests/<int:lab_test_id>', methods=['PUT'])
def update_lab_test(lab_test_id):
    # TODO: Implement update_lab_test endpoint
    pass


@lab_tests_api_bp.route('/lab_tests/<int:lab_test_id>', methods=['DELETE'])
def delete_lab_test(lab_test_id):
    # TODO: Implement delete_lab_test endpoint
    pass
