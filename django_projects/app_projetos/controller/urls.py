from django.urls import path 
from controller.views import ProjetoListAPIView, EquipeListAPIView


# /api/projetos/
urlpatterns = [
    path('projetos/', ProjetoListAPIView.as_view()),
    path('equipes/', EquipeListAPIView.as_view()),
]