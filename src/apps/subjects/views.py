from django.shortcuts import render
from django.http import HttpResponse

def all_subjects(request):
    return HttpResponse("<h1>All subjects</h1>")

