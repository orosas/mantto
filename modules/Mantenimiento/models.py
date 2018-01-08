from django.db import models

# Create your models here.
'''
Crear class Contratista ligado a class Mops

Crear class Mopslog para hacer tracker de cambios de mops


'''


class Sitio(models.Model):
	site = models.CharField(max_length=80, null=False, blank=False)
	site_name = models.CharField(max_length=100, null=False, blank=False)
	iden = models.CharField(max_length=80, null=True, blank=True)
	gsm = models.CharField(max_length=100, null=True, blank=True)
	id_3g = models.CharField(max_length=100, null=True, blank=True)
	lte = models.CharField(max_length=100, null=True, blank=True)
	lat_decimal = models.DecimalField(max_digits=9, decimal_places=6, null=True)
	long_decimal = models.DecimalField(max_digits=9, decimal_places=6, null=True)
	site2 = models.CharField(max_length=80, null=True, blank=True)
	jerarquia = models.CharField(max_length=50, null=True, blank=True)
	jerarquia_modif = models.CharField(max_length=50, null=True, blank=True)
	co = models.CharField(max_length=100, null=True, blank=True)
	co_celular = models.CharField(max_length=100, null=True, blank=True)
	co_email = models.CharField(max_length=100, null=True, blank=True)
	coord = models.CharField(max_length=100, null=True, blank=True)
	coord_celular = models.CharField(max_length=50, null=True, blank=True)
	coord_email = models.CharField(max_length=100, null=True, blank=True)
	manager = models.CharField(max_length=100, null=True, blank=True)
	manager_celular = models.CharField(max_length=50, null=True, blank=True)
	manager_email = models.CharField(max_length=100, null=True, blank=True)
	director = models.CharField(max_length=100, null=True, blank=True)
	director_celular = models.CharField(max_length=50, null=True, blank=True)
	director_email = models.CharField(max_length=100, null=True, blank=True)
	coordination = models.CharField(max_length=50, null=True, blank=True)
	management = models.CharField(max_length=50, null=True, blank=True)
	region = models.CharField(max_length=20, null=True, blank=True)
	region_num = models.CharField(max_length=4, null=True, blank=True)
	mercado_ciudad = models.CharField(max_length=100, null=True, blank=True)
	mercado_anterior = models.CharField(max_length=100, null=True, blank=True)
	prioridad = models.CharField(max_length=4, null=True, blank=True)
	tipo_ante = models.CharField(max_length=50, null=True, blank=True)
	capacidad_gen = models.CharField(max_length=20, null=True, blank=True)
	cobertura_min = models.CharField(max_length=100, null=True, blank=True)
	acceso = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	municipality = models.CharField(max_length=100, null=True, blank=True)
	state_name = models.CharField(max_length=50, null=True, blank=True)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	capturado_por = models.OneToOneField(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s" % (self.site_name)


MES = (
		('Enero','Enero'),
		('Febrero','Febrero'),
		('Marzo','Marzo'),
		('Abril','Abril'),
		('Mayo','Mayo'),
		('Junio','Junio'),
		('Julio','Julio'),
		('Agosto','Agosto'),
		('Septiembre','Septiembre'),
		('Octubre','Octubre'),
		('Noviembre','Noviembre'),
		('Diciembre','Diciembre'),
	)



class Mops(models.Model):
	site = models.ForeignKey(Sitio, on_delete=models.CASCADE,)
	tipo_mop = models.CharField(max_length=100, null=True, blank=True)
	cantidad_mop = models.PositiveSmallIntegerField()
	mes_programado = models.CharField(choices=MES, max_length=50, null=False, blank=False)
	fecha_inicio = models.DateField(null=True, blank=True)
	fecha_fin = models.DateField(null=True, blank=True)
	contratista = models.OneToOneField(Contratista, on_delete=models.CASCADE,)
	reporte_recibido = models.DateField(null=True, blank=True)
	reporte_enviado = models.DateField(null=True, blank=True)
	reporte_validado = models.DateField(null=True, blank=True)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	capturado_por = models.OneToOneField(User, on_delete=models.CASCADE,)