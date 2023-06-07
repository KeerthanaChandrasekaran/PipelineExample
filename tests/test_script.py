import pytest
import inspect
import logging

# setting log details
loggerName = inspect.stack()[1][3]
logger = logging.getLogger(loggerName)

# creating log file
fileHandler = logging.FileHandler('logReport.log')

# defining the formatter and setting it for log file
formatter = logging.Formatter(
    "%(asctime)s : %(levelname)s : %(name)s : %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)

def test_one():
    logger.info('Test One Status: Success')
    assert 1 == 1


def test_two():
    logger.debug('Test Two')
    assert True, 'Valid Case'
