from django.contrib import admin

from .models import Vehicle

admin.site.site_header = 'Parking Cloud Admin'
admin.site.site_title = 'Parking Cloud Admin Area'
admin.site.index_title = 'Bienvenido al área de administración de Parking Cloud'
admin.site.register(Vehicle)