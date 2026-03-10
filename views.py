from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice, Submission


def submit(request):
    return HttpResponse("Exam submitted successfully")


def show_exam_result(request):
    return HttpResponse("Exam result displayed")
