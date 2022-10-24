from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Case

@login_required
def cases(request):
    context = {
        'cases': Case.objects.all()
    }
    return render(request, 'cases/cases.html', context)