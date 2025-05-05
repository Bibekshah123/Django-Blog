import time
from django.utils.deprecation import MiddlewareMixin

class SimpleLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
        
    def process_response(self, request, response):
        total_time = time.time() - getattr(request, 'start_time', time.time())
        print(f"[LOG] {request.method} {request.path} took {total_time:.2f}s")
        return response
    
    