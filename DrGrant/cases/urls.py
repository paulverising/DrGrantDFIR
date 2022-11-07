from django.urls import path
from .views import CasesListView, CasesDetailView, CasesCreateView, CasesUpdateView, CasesDeleteView, UserCasesListView, case_list

urlpatterns = [
    path('', CasesListView.as_view(), name='Cases'),
    path('<int:pk>/', CasesDetailView.as_view(), name='cases-detail'),
    path('new/', CasesCreateView.as_view(), name='cases-create'),
    path('<int:pk>/update', CasesUpdateView.as_view(), name='cases-update'),
    path('<int:pk>/delete', CasesDeleteView.as_view(), name='cases-delete'),
    path('user/<str:username>/', UserCasesListView.as_view(), name='user-cases'),
    path('cases/', case_list)
]