from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        # este if se ejecuta siempre y cuando por url venga el slug
        # el slug es el campo de la tabla, y lo compara con el slug que entra por URL
        # si no lo encuentra tira una excepción de tipo 404, pagina no encontrada
        categories = get_object_or_404(Category, slug=category_slug)
        # aqui se filtra la información por la categoria y por si esta habilitado
        products = Product.objects.filter(category = categories, is_available = True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()

    context = {
        'products' : products,
        'product_count':product_count,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        # esta es la consulta a la base de datos
        #el primir slug tiene dos _ para hacer referencia al campo de la base
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    # el resultado de la consulta se almacena en un diccionario
    context = {
        'single_product': single_product,
    }
    # aqui es donde se indica el template que mostrara la función, le pasa el nombre de la pagina y el diccionario con el resultado de la consulta a base de datos
    return render(request, 'store/product_detail.html', context)
