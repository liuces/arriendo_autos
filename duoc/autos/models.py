from django.db import models

# Create your models here.

class cliente (models.Model):
    nombre_cliente = models.CharField(max_length=30)
    ape_cliente = models.CharField(max_length=30)
    email_cliente = models.CharField(max_length=50)
    contrasena_cliente = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    direccion_cliente = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre_cliente} {self.ape_cliente}"

class automovil (models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    nombre_automovil = models.CharField(max_length=30)
    descripcion_automovil = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='autos/')

    def __str__(self):
        return f"{self.nombre_automovil}"

class arriendo (models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    sucursal = models.CharField(max_length=30)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    automovil = models.ForeignKey(automovil, on_delete=models.CASCADE)

    def __str__(self):
        return f"Arrendamiento de {self.automovil} por {self.cliente} desde {self.fecha_inicio} hasta {self.fecha_fin}"

class administrador (models.Model):
    nombre_admin = models.CharField(max_length=30)
    ape_admin = models.CharField(max_length=30)
    usuario_admin = models.CharField(max_length=30)
    email_admin = models.CharField(max_length=50)
    contrasena_admin = models.CharField(max_length=30)
    fecha_nacimiento_admin = models.DateField()
    direccion_admin = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre_admin} {self.ape_admin}"