


# Run quote calculation if this module is the main script
from test import run_test_quote
from logger import LOGGER


__LOGGER = LOGGER

if __name__ == "__main__":
    __LOGGER.info("This is an insurance quote algorithm")
    run_test_quote()

