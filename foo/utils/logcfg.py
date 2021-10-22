import logging
from logging.handlers import RotatingFileHandler


class LogUtil(object):
    def __init__(self):
        self.log_path = '../../static/file.log'
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)

        # 一个终端处理器
        terminal_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.sh = logging.StreamHandler()
        # 设置单独的终端处理显示信息
        self.sh.setLevel(logging.INFO)
        self.sh.setFormatter(terminal_formatter)

        # 一个文件处理器
        file_formatter = logging.Formatter('[%(asctime)s] - %(lineno)d - %(name)s\n'
                                           '======%(threadName)s - %(funcName)s - %(filename)s\n'
                                           '======%(levelname)s - %(levelno)s - %(message)s')
        self.rfh = RotatingFileHandler(self.log_path, 'a', 3 * 1024 * 1024, 10)
        self.rfh.setLevel(logging.DEBUG)
        self.rfh.setFormatter(file_formatter)

        self.log.addHandler(self.sh)
        self.log.addHandler(self.rfh)

        # 据说有可能会出现打印两次失败的情况
        self.sh.close()
        self.rfh.close()

    def get_log(self):
        return self.log


logger = LogUtil().get_log()


logger.debug('----debug')
logger.info('----info')
logger.error('-----error')