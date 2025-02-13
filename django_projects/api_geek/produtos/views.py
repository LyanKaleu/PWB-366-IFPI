from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Produto, Categoria, Franquia
from .serializers import ProdutoSerializer, CategoriaSerializer, FranquiaSerializer, ReporEstoqueSerializer
from .filters import ProdutoFilter
from .pagination import CustomPagination
from usuarios.permissions import IsVendedor
from .models import Produto
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FranquiaViewSet(viewsets.ModelViewSet):
    queryset = Franquia.objects.all()
    serializer_class = FranquiaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Endpoint para gerenciar produtos.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProdutoFilter
    search_fields = ['nome', 'descricao']
    pagination_class = CustomPagination
    ordering_fields = ['nome', 'preco', 'quantidade_estoque']
    permission_classes = [IsAuthenticated, IsVendedor]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    def destroy(self, request, *args, **kwargs):
        produto = self.get_object()

        if produto.quantidade_estoque != 0:
            return Response(
                {"error": "Produto não pode ser excluído porque ainda há estoque."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(
            method='patch',
            request_body=ReporEstoqueSerializer,
            responses={status.HTTP_200_OK: ProdutoSerializer}
    )
    @action(detail=True, methods=['patch'], url_path='repor-estoque')
    def repor_estoque(self, request, pk=None):
        produto = self.get_object()
        serializer = ReporEstoqueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quantidade = serializer.validated_data['quantidade']
        produto.quantidade_estoque += quantidade
        produto.save()

        return Response(
            {"id": produto.id, "quantidade_estoque": produto.quantidade_estoque},
            status=status.HTTP_200_OK
        )
        