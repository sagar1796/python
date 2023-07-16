import logging
#five different log level
logging.basicConfig(level=logging.INFO, format="{asctime} {message}", style='{')
logging.debug("This is a debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is a critical message")

