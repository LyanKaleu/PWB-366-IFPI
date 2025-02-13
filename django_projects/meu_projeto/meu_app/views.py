from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Produto, Cliente, Pedido


# VIEWS BASEADAS EM FUNÇÃO (FUNCTION-BASED VIEWS)
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return HttpResponse(clientes)


def detalhe_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        return JsonResponse(cliente)
    except Cliente.DoesNotExist:
        return JsonResponse({'erro': 'Cliente não encontrado'}, status=404)
    

# VIEWS BASEADAS EM CLASSES (CLASS-BASED VIEWS)
class ListarProdutosView(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return JsonResponse(list(produtos), safe=False)
