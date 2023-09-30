from .prescriptions import *
from .patients import *
from .lab_tests import *
from .doctors import *
from .appointments import *
from flask import Blueprint

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
