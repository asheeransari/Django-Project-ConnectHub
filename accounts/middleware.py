import time
import logging

logger = logging.getLogger("performance")


class PerformanceLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.perf_counter()

        response = self.get_response(request)

        total_time = time.perf_counter() - start_time

        logger.info(
            "PERFORMANCE | method=%s | path=%s | status=%s | time=%.4f seconds",
            request.method,
            request.path,
            response.status_code,
            total_time,
        )

        return response