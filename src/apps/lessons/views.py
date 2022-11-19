from django.shortcuts import render
from django.http import HttpResponse

def all_lessons(request):
    return HttpResponse("<h1>All lessons</h1>")
