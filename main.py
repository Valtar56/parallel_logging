from datetime import datetime as dt
from clogging import *

dir_path = BASE_DIR
time_run = dt.now()
dt_string = time_run.strftime("%d-%m-%Y")
log_fname = '%s' % dt_string

dlogger = setup_logger(log_fname, LOGGING_PATH +
                       '/log_%s.log' % dt_string, level=logging.DEBUG)

def multiply(a, b):
    dlogger.debug(f'The numbers input are: {a} and {b}')
    result = a*b
    dlogger.debug(f'The result is {result}')
    return result

if __name__ == "__main__":
    multiply(4, 2)