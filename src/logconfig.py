import logging

LOGGER = logging.Logger(__name__)
LOGGER.setLevel(logging.DEBUG)
FILE_HANDLER = logging.FileHandler('logfile.log')
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(FILE_HANDLER)
#logging.basicConfig(filename=FILE_HANDLER, format=FORMATTER, level=logging.DEBUG)
