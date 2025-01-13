from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World! Polls index!!!")


def polls_add(request):
    return HttpResponse("New poll!!")


def detail(request, question_id):
    return HttpResponse(f"You´re looking at question {question_id}")


def results(request, question_id):
    response = f"You´re looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You´re voting on question {question_id}")
