import logging
def get_logger():
    logger = logging.getLogger("framework")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("framework.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(fh)

    return logger
