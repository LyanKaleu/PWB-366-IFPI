from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, CategoriaViewSet, FranquiaViewSet


router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'franquias', FranquiaViewSet)
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
