from .models import Category
# es para la función de filtrar por categorias en la pagina store

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
