from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.


class automovil (models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    nombre_automovil = models.CharField(max_length=30)
    descripcion_automovil = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='autos/')

    def __str__(self):
        return f"{self.nombre_automovil}"

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)

    def __str__(self):
        return self.user.username + ' - ' + self.role