from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
# se registra la clase dentro del modelo

# PARA PERSONALIZAR LAS COLUMNAS QUE SE MUESTRAN EN LA ADMINISTRACIÓN DEL Django
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Account, AccountAdmin)
