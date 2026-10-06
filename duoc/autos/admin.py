from django.contrib import admin
from .models import cliente, automovil, arriendo, administrador
# Register your models here.

admin.site.register(cliente)
admin.site.register(automovil)
admin.site.register(arriendo)
admin.site.register(administrador)