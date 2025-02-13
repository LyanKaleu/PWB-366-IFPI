from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsCliente
from usuarios.models import Usuario
from .models import Venda
from .serializers import VendaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated, IsCliente]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Venda.objects.all()
        
        usuario = Usuario.objects.get(username=self.request.user.username)
        return Venda.objects.filter(cliente=usuario)
