from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projeto, Equipe, Comentario
from .serializers import ComentarioSerializer, ProjetoSerializer, EquipeSerializer
from rest_framework import generics, viewsets


# Viewset para o comentário
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


# POST e GET em /api/equipes/
class EquipeListCreateView(generics.ListCreateAPIView):
    # get() da mãe, e list() da vó
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


# GET, PUT e DELETE em /api/equipes/<int:pk>/
class EquipeDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class ProjetoListAPIView(APIView):
    # GET /api/projetos/
    def get(self, request):
        projetos = Projeto.objects.all()
        serializer = ProjetoSerializer(projetos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjetoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


# class EquipeListAPIView(APIView):
#     # GET /api/equipes/
#     def get(self, request):
#         equipes = Equipe.objects.all()
#         serializer = EquipeSerializer(equipes, many=True)
#         return Response(serializer.data)
    