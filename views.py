from django.shortcuts import render
from django.http import HttpResponse


def submit(request):
    return HttpResponse("Submission successful")


def show_exam_result(request):
    return HttpResponse("Exam result")
