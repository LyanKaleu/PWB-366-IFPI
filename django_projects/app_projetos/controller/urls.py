from django.urls import path, include 
from controller.views import ProjetoListAPIView #, EquipeListAPIView
from controller.views import ComentarioViewSet, EquipeListCreateView, EquipeDetailUpdateDestroyView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)

# /api/projetos/
urlpatterns = [
    path('projetos/', ProjetoListAPIView.as_view()),
    path('equipes/', EquipeListCreateView.as_view()),
    path('equipes/<int:pk>/', EquipeDetailUpdateDestroyView.as_view()),
    path('', include(router.urls)),
    # path('equipes/', EquipeListAPIView.as_view()),
]