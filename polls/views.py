from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import render, get_object_or_404


def detail(request: HttpResponse, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)

def results(request: HttpResponse, question_id: int):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request: HttpResponse, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}")

def index(request: HttpResponse):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)
