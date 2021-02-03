from flask import current_app
from flask_restful import Resource, reqparse

from common.logging import logged


class Start(Resource):
    def get(self):
        # logger.info('-----get request-----')
        current_app.logger.info('-----current ----log')
        logged.info('----- set up logger ------')
        return 'hello world'

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        args = parser.parse_args()

        rate = args.rate
        return {
            "rate": rate
        }
