import logging

"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")  # defualt levl is warning n above
logging.error("This is a error message")
logging.critical("This is a critical message")
"""

logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("this is an error")

# https://chatgpt.com/c/696fb60a-11f4-8320-8919-ff3ff9b1a68b explanation

"""
                    👦 LOGGER
               (warning / error)
                         |
            --------------------------------
            |                              |
      📺 StreamHandler               📒 FileHandler
   (WARNING and up)                 (ERROR and up)
            |                              |
       shows on screen              writes to file.log

"""

# named loggers propagate to root by default.
