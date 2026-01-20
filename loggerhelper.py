import logging

logger = logging.getLogger(
    __name__
)  # here it is logger is loggerhelper name = main or imported file
logger.propagate = False  # default true
logger.info("hello from helper")
