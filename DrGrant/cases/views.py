from typing import OrderedDict
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Case
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
# def cases(request):
#     context = {
#         'cases': Case.objects.all()
#     }

#     return render(request, 'cases/cases.html', context)


class CasesListView(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'cases/cases.html'
    context_object_name = 'cases'
    ordering = ['-dateCreated']

class CasesDetailView(LoginRequiredMixin, DetailView):
    model = Case

class CasesCreateView(LoginRequiredMixin, CreateView):
    model = Case
    fields = ['name', 'description']

class CasesUpdateView(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ['name', 'description']

class CasesDeleteView(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = '/'