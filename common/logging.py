import logging
from logging.handlers import RotatingFileHandler

from flask import has_request_context, request


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


formatters = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)

flask_file_handle = RotatingFileHandler('static/logg.log', 'a', 300 * 1024 * 1024, 10)
flask_file_handle.setFormatter(formatters)

formatter = logging.Formatter('[%(asctime)s]%(filename)s-%(funcName)s-%(lineno)d\n-%(message)s')

file_handle = RotatingFileHandler('static/lo.log', 'a', 300 * 1024 * 1024, 10)
file_handle.setFormatter(formatter)

# 如果把pass改成__name__会打印两次日志
logged = logging.getLogger('pass')
logged.addHandler(file_handle)
logged.setLevel("DEBUG")
