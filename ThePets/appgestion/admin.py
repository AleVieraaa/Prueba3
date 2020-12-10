from django.contrib import admin

# Register your models here.
from appgestion.models import Cliente,Mascota
admin.site.register(Cliente)
admin.site.register(Mascota)