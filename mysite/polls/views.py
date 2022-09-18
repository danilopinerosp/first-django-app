from http.client import HTTPResponse
from django.http import HttpResponse

def index(request):
    return HTTPResponse("Hello, world. You're at the polls index.")
