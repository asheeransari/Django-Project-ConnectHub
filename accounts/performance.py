import time
import logging
from functools import wraps

logger = logging.getLogger("performance")


def log_performance(feature_name):
    def decorator(view_func):

        @wraps(view_func)
        def wrapper(*args, **kwargs):

            start_time = time.perf_counter()

            try:
                return view_func(*args, **kwargs)

            finally:
                total_time = time.perf_counter() - start_time

                logger.info(
                    "PERFORMANCE | feature=%s | time=%.4f seconds",
                    feature_name,
                    total_time,
                )

        return wrapper

    return decorator