from ctypes.wintypes import HRSRC
from django.http import HttpResponse

def detail(request: HttpResponse, question_id: int):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request: HttpResponse, question_id: int):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request: HttpResponse, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}")

def index(request: HttpResponse):
    return HttpResponse("Hello, world. You're at the polls index.")
