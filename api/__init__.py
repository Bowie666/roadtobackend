from flask import Blueprint
from flask_restful import Api

from .start import Start


func_bp = Blueprint('api', __name__)
func_api = Api(func_bp)

func_api.add_resource(Start, '/', '/index')
