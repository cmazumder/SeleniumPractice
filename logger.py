import logging
import sys
from os import mkdir, path


class Logger:

    def __init__(self, log_path, file_name, log_level=logging.INFO, info="Browser search performance | using Selenium"):
        logging.basicConfig(filename=log_path + file_name,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=log_level)
        logging.info(info)

        formatter = logging.Formatter(fmt='%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')  # %I:%M:%S %p AM|PM format

        # console printer
        screen_handler = logging.StreamHandler(stream=sys.stdout)  # stream=sys.stdout is similar to normal print
        screen_handler.setFormatter(formatter)
        logging.getLogger().addHandler(screen_handler)

        self.logging = logging.getLogger('BrowserPerformance_logger')

    def __del__(self):
        self.logging.info("Exit execution")

    def get_instance(self):
        return self.logging


file_name_local = 'SeleniumPractice.log'
file_path_local = r"Logs\\"

try:
    if not path.isdir(file_name_local):
        mkdir(file_name_local)
    logger_object = Logger(log_path=file_path_local, file_name=file_name_local, log_level=logging.INFO)
except Exception as err:
    print err.message
