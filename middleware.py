from django.utils.deprecation import MiddlewareMixin


# class CustomHeaderMiddleware(MiddlewareMixin):
#     """
#     Class Name: CustomHeaderMiddleware.
#
#     Description: Middleware to process requests before they reach their respective view classes.
#     """
#     @classmethod
#     def process_request(self, request):
#         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
class BaseTestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Start', self.middleware_name)
        response = self.get_response(request)
        print('End', self.middleware_name)


class TestMiddleware1(BaseTestMiddleware):
    middleware_name = "First Middleware"


class TestMiddleware2(BaseTestMiddleware):
    middleware_name = "Second Middleware"


class TestMiddleware3(BaseTestMiddleware):
    middleware_name = "Third Middleware"
