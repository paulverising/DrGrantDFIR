from typing import OrderedDict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    paginate_by = 5

class UserCasesListView(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'cases/user_cases.html'
    context_object_name = 'cases'
    ordering = ['-dateCreated']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Case.objects.filter(incidentManager=user)

class CasesDetailView(LoginRequiredMixin, DetailView):
    model = Case

class CasesCreateView(LoginRequiredMixin, CreateView):
    model = Case
    fields = ['name', 'incidentManager', 'description']

class CasesUpdateView(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ['name', 'incidentManager', 'description']

class CasesDeleteView(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = '/'