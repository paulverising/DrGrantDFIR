from django.shortcuts import render
from django.http import HttpResponse

def cases(request):
    return render(request, 'cases/cases.html')