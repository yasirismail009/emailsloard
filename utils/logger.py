import logging

logging.basicConfig(
    filename="emailsloard.error.log",
    format='[%(asctime)s] %(levelname)s (%(pathname)s) \"%(message)s\"',
    datefmt='%d/%b/%Y %H:%M:%S',
    filemode='w'
)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
