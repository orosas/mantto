from django.contrib import admin
from .models import Sitio, Contratista, Mops, Mopslog

# Register your models here.

class SitioAdmin(admin.ModelAdmin):
	search_fields = ('site', 'site_name', 'iden', 'gsm')

	# despliega todos éstos campos en el Admin, antes de ver detalles de cada registro
	list_display = ('site', 'site_name',)

	# agrega una barra del lado derecho para poder filtrar los resultados
	list_filter = ('coord', )


class MopsAdmin(admin.ModelAdmin):
	search_fields = ('site', 'tipo_mop', )

	# despliega todos éstos campos en el Admin, antes de ver detalles de cada registro
	list_display = ('site', 'tipo_mop', 'mes_programado',)

	# agrega una barra del lado derecho para poder filtrar los resultados
	list_filter = ('tipo_mop', 'mes_programado')

admin.site.register(Sitio, SitioAdmin)
admin.site.register(Mops, MopsAdmin)


