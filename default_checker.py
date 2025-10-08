import logging

def check_defaults(obj, path="", logger = None):
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.warning(f"No logger was provided to function {check_defaults.__name__}")
    
    if obj is None:
        logger.error("Cant check defaults for oobj because it is none")
        return

    for attr, value in vars(obj).items():
        full_path = f"{path}.{attr}" if path else attr
        if isinstance(value, int) and value == -1:
            logger.warning(f"Warning: {full_path} is using default value -1")
        elif isinstance(value, str) and (value is None or value.strip() == ""):
            logger.warning(f"Warning: {full_path} is not set")
        elif isinstance(value, list) and (value is None or len(value) == 0):
            logger.warning(f"Warning: {full_path} list is empty or not set")
        elif value is None:
            logger.warning(f"Warning: {full_path} is None")