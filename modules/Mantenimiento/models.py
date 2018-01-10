from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''
ToDo: OMAR

09-ENE-2018
Crear class tracker de correctivos


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
	coord_mastec = models.CharField(max_length=100, null=True, blank=True)
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
	# Relación OneToOne tiene que ser unique
	capturado_por = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s" % (self.site + " " + self.site_name)


class Contratista(models.Model):
	nombre_contratista = models.CharField(max_length=100, null=False, blank=False)
	razon_social = models.CharField(max_length=100, null=True, blank=True)
	contacto = models.CharField(max_length=100, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	telefono = models.CharField(max_length=50, null=True, blank=True)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	capturado_por = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s" % (self.nombre_contratista)

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
	tipo_mop = models.CharField(max_length=100, null=False, blank=False)
	cantidad_mop = models.PositiveSmallIntegerField(null=False, blank=False)
	mes_programado = models.CharField(choices=MES, max_length=50, null=False, blank=False)
	semana_programada = models.PositiveSmallIntegerField(null=True, blank=True)
	fecha_inicio = models.DateField(null=True, blank=True)
	fecha_fin = models.DateField(null=True, blank=True)
	contratista = models.OneToOneField(Contratista, on_delete=models.CASCADE, null=True, blank=True)
	lider_contratista = models.CharField(max_length=100, null=True, blank=True)
	# Fechas para seguimiento temporal, ya que la idea es que
	# con la cadena de autorización se registren la fechas
	reporte_recibido = models.DateField(null=True, blank=True)
	reporte_enviado_co = models.DateField(null=True, blank=True)
	reporte_validado_co = models.DateField(null=True, blank=True)
	reporte_enviado_coord = models.DateField(null=True, blank=True)
	reporte_validado_coord = models.DateField(null=True, blank=True)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	capturado_por = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s" % (self.tipo_mop)

class Mopslog(models.Model):
	site_log = models.ForeignKey(Sitio, on_delete=models.CASCADE,)
	tipo_mop_log = models.CharField(max_length=100, null=False, blank=False)
	cantidad_mop_log = models.PositiveSmallIntegerField(null=False, blank=False)
	mes_programado_log = models.CharField(choices=MES, max_length=50, null=False, blank=False)
	semana_programada_log = models.PositiveSmallIntegerField(null=True, blank=True)
	fecha_inicio_log = models.DateField(null=True, blank=True)
	fecha_fin_log = models.DateField(null=True, blank=True)
	contratista_log = models.OneToOneField(Contratista, on_delete=models.CASCADE, null=True, blank=True)
	lider_contratista_log = models.CharField(max_length=100, null=True, blank=True)
	# Fechas para seguimiento temporal, ya que la idea es que
	# con la cadena de autorización se registren la fechas
	reporte_recibido_log = models.DateField(null=True, blank=True)
	reporte_enviado_co_log = models.DateField(null=True, blank=True)
	reporte_validado_co_log = models.DateField(null=True, blank=True)
	reporte_enviado_coord_log = models.DateField(null=True, blank=True)
	reporte_validado_coord_log = models.DateField(null=True, blank=True)
	fecha_modif_log = models.DateField(auto_now=True)
	fecha_creacion_log = models.DateField(auto_now_add=True)
	capturado_por_log = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s" % (self.tipo_mop_log)