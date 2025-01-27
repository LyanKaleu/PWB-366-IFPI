from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projeto
from .serializers import ProjetoSerializer


class ProjetoListAPIView(APIView):
    # GET /api/projetos/
    def get(self, request):
        projetos = Projeto.objects.all()
        serializer = ProjetoSerializer(projetos, many=True)
        return Response(serializer.data)
