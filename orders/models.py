from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings

User = get_user_model() #Toma le modelo del ususario que vamos a crear

# Create your models here.
class Toppings(models.Model):
    nombre = models.CharField(max_length=35)
    precio = models.DecimalField(max_digits=4,null=True, blank=True, default=00.00, decimal_places=2)

    def _str_(self):
        return f"(self.nombre)"

class menu(models.Model):
    categorias= (
        ('pizza', 'pizza'),
        ('pasta', 'pasta'),
        ('Dinner Platters', 'Dinner PLatters'),
    )

    tamano = (
        ('SM', 'Small'),
        ('L', 'Large'),
    )

    nombre = models.CharField(max_length=35, null=True, blank=True)

    categoria = models.CharField(max_length =15, null=True,blank=True, choices= categorias) #Choices le estamos diciendo que escoja entre las opciones del diccionario categorias

    precio = models.DecimalField(max_digits=4, null=True, blank=True, decimal_places=2, default=0.00)

    tamano = models.CharField(max_length =30, null=True,blank=True, choices= tamano)

    toppings = models.CharField(max_length =30, null=True,blank=True)

    cantidad_toppings = models.CharField(max_length =30, null=True,blank=True)

    def __str__ (self):
        return f"Categoria:{self.nombre} - {self.categoria} - {self.precio} - {self.tamano} - {self.toppings} - {self.cantidad_toppings}"

class user(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu = models.ManyToManyField(menu, blank=True)

    def __str__(self):
        return f"{self.user}"

def create_user(sender, instance, created, *args, **kwargs):
    if created:
        user_profile, created = user.objects.get_or_create(user = instance)

post_save.connect(create_user, sender=settings.AUTH_USER_MODEL)