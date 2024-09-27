from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # imnportaciones necesarias para manejar la creación y administración de usuarios
# Create your models here.

# esta clase es para las operaciones de crear usuarios y super admin usuario
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
# para guardar en la base de datos
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        # seteo de atributos que debe tener el admin
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # los de ahora son por defecto de django que se deben declarar
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # aqui se setea para que el usuario se logee por correo y no por user_name
    USERNAME_FIELD = 'email'

    # PARA DECIR CUALES SON LOS CAMPOS OBLIGATORIOS
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

# para instanciar la clase de super usuario
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # funcion es para saber si tiene permisos de administración
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # si es administrador debe tener permiso para los modulos
    def has_module_perms(self, add_label):
        return True
