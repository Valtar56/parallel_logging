from __future__ import absolute_import
import logging
import os
import warnings
warnings.filterwarnings("ignore")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGING_PATH = BASE_DIR + '/logs'

if not os.path.exists(LOGGING_PATH):
    os.makedirs(LOGGING_PATH)


def setup_logger(logger_name, log_file, mode='a', level=None):
    """As the name suggests, it is a logger function

    Args:
        logger_name (name of the logger file): _description_
        log_file (_type_): _description_
        mode (str, optional): _description_. Defaults to 'a'.
        level (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """    
    if logger_name in logging.Logger.manager.loggerDict:
        return logging.getLogger(logger_name)
    else:
        l = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        fileHandler = logging.FileHandler(log_file, mode=mode)
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        l.setLevel(level)
        l.addHandler(fileHandler)
        l.addHandler(streamHandler)

        return l