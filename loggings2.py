import logging

"""
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(
        e, exc_info=True
    )  # the root logger is called because getlogger isnt used
"""
import traceback  # if im unaware of the type of error raised

try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error("This error is %s", traceback.format_exc())
