from rest_framework import viewsets, permissions
from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()] 
        return super().get_permissions()
    