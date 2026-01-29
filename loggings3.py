import logging
from logging.handlers import RotatingFileHandler as rfl

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = rfl("app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("hello, world")

"""
import time
from logging.handlers import TimedRotatingFileHandler as trfl

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#s,m,h,d, midnight, w0
handler = trfl('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('hello, world')
    time.sleep(5)
"""
