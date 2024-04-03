from django.contrib import admin
from Ventas.models import Venta

class VentasAdmin(admin.ModelAdmin):
   list_display = ["Cliente", "Barrio", "Mes"]
   lsit_search=["Mes"]

admin.site.register(Venta, VentasAdmin)