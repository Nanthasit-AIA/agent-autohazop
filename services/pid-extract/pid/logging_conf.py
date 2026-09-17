import logging, os, time
from functools import wraps

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s",
)
logger = logging.getLogger("pid-extract")

def timeit_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.debug(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        logger.debug(f"Finished: {func.__name__} in [Time] {duration:.4f} sec")
        return result
    return wrapper
