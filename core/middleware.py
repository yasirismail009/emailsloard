from django.http import HttpResponseForbidden
from core import secrets


class ApiSecretMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Request header `Api-Secret` becomes `HTTP_API_SECRET`
        # Read more: https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.META
        secret = request.META.get("HTTP_API_SECRET")

        if not (secret and secret == secrets.HTTP_API_SECRET):
            return HttpResponseForbidden()

        response = self.get_response(request)
        return response
