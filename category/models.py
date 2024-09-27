from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique = True)
    description = models.CharField(max_length=255, blank = True)
    # es un concepto que se utiliza en e-commerce
    slug = models.CharField(max_length=100, unique = True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)

    # ESTE META ES PARA CAMBIAR EL NOMBRE EN LA ESTRUCTURA DE LA BASE DE DATOS POR EL PLURAL CATEGORIES
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


# es el def para el filtro por categorias

    def get_url(self):
        # recrea la url de store y le suma el slug para que la tome por metodo get
        return reverse('products_by_category', args=[self.slug])



    # la data sera visible desde el modulo de administración de django, para eso esto:

    def __str__(self):
        return self.category_name
