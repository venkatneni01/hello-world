import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('myapp')

def log_one():
    # Log debug messages
    logger.debug("print_logs")
    logger.debug("print_debug")
    
    # This will cause a ZeroDivisionError
    try:
        1/0
    except Exception as e:
        # Log the exception with traceback
        logger.exception("Exception occurred")

if __name__ == '__main__':
    log_one()





