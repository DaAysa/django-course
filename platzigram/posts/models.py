# Django
from django.db import models

class User(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField()

    birthdate = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

"""
python3 manage.py shell
from posts.models import User

daiana = User.objects.create(
...     email='email@email.com',
...     password='12345678',
...     first_name='Daiana',
...     last_name='Aysa',
... )

Modificar campo:
daiana.email='daiana@email.com'
daiana.save()

Otra forma de crear:
arturo = User()
arturo.email=...
arturo.password=...
arturo.first_name=...
arturo.last_name=...
arturo.save()

arturo.delete()


Traer un objeto de la db:
user = User.objects.get(email='freddier@platzi.com')

Hacer un query:
platzi_users = User.objects.filter(email__endswith='@platzi.com')

Hacer mismo update a todos los del query:
platzi_users = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)

Traer todos:
users = User.objects.all()
"""


"""
Utilizando el modelo user con el que ya viene django por defecto
from django.contrib.auth.models import User

user = User.objects.create_user(username='Daiana', password='123456')


"""