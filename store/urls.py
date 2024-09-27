from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    # views.product_detail este es el nombre de la función que va a direccionar a la pagina producto, idem a la linea anterior
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
