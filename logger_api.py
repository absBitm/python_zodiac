import logging
import logging.handlers

default_log_dir = '/var/log/'


def get_sensor_logger(topic, log_dir=default_log_dir):
    logger = logging.getLogger(str(topic))
    logger.setLevel(logging.DEBUG)

    fh0 = logging.FileHandler(log_dir + 'sensor_info.log')
    fh0.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)7s - %(name)s - [ %(filename)s:%(lineno)s - %(funcName)25s() ] %(message)s')
    fh0.setFormatter(formatter)

    fh1 = logging.FileHandler(log_dir + 'sensor_debug.log')
    fh1.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)7s - %(name)s - [ %(filename)s:%(lineno)s - %(funcName)25s() ] %(message)s')
    fh1.setFormatter(formatter)

    if len(logger.handlers) > 0:
        for handler in logger.handlers:
            if not isinstance(handler, logging.FileHandler):
                logger.addHandler(fh0)
                logger.addHandler(fh1)
    else:
        logger.addHandler(fh0)
        logger.addHandler(fh1)

    return logger


sensor_logger = get_sensor_logger('sensor')
