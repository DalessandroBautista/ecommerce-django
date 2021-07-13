from .models import Categoria

def importe_total_carro (request):
    total=0
    if request.user.is_authenticated and 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
    return {"importe_total_carro":total}



def categorias_bd(request):

    link_categorias = Categoria.objects.all()
    return {
        'link_categorias': link_categorias
    }