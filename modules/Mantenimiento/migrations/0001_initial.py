# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-09 23:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_contratista', models.CharField(max_length=100)),
                ('razon_social', models.CharField(blank=True, max_length=100, null=True)),
                ('contacto', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_modif', models.DateField(auto_now=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('capturado_por', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_mop', models.CharField(max_length=100)),
                ('cantidad_mop', models.PositiveSmallIntegerField()),
                ('mes_programado', models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=50)),
                ('semana_programada', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('lider_contratista', models.CharField(blank=True, max_length=100, null=True)),
                ('reporte_recibido', models.DateField(blank=True, null=True)),
                ('reporte_enviado_co', models.DateField(blank=True, null=True)),
                ('reporte_validado_co', models.DateField(blank=True, null=True)),
                ('reporte_enviado_coord', models.DateField(blank=True, null=True)),
                ('reporte_validado_coord', models.DateField(blank=True, null=True)),
                ('fecha_modif', models.DateField(auto_now=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('capturado_por', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contratista', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Mantenimiento.Contratista')),
            ],
        ),
        migrations.CreateModel(
            name='Mopslog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_mop_log', models.CharField(max_length=100)),
                ('cantidad_mop_log', models.PositiveSmallIntegerField()),
                ('mes_programado_log', models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=50)),
                ('semana_programada_log', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('fecha_inicio_log', models.DateField(blank=True, null=True)),
                ('fecha_fin_log', models.DateField(blank=True, null=True)),
                ('lider_contratista_log', models.CharField(blank=True, max_length=100, null=True)),
                ('reporte_recibido_log', models.DateField(blank=True, null=True)),
                ('reporte_enviado_co_log', models.DateField(blank=True, null=True)),
                ('reporte_validado_co_log', models.DateField(blank=True, null=True)),
                ('reporte_enviado_coord_log', models.DateField(blank=True, null=True)),
                ('reporte_validado_coord_log', models.DateField(blank=True, null=True)),
                ('fecha_modif_log', models.DateField(auto_now=True)),
                ('fecha_creacion_log', models.DateField(auto_now_add=True)),
                ('capturado_por_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contratista_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Mantenimiento.Contratista')),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=80)),
                ('site_name', models.CharField(max_length=100)),
                ('iden', models.CharField(blank=True, max_length=80, null=True)),
                ('gsm', models.CharField(blank=True, max_length=100, null=True)),
                ('id_3g', models.CharField(blank=True, max_length=100, null=True)),
                ('lte', models.CharField(blank=True, max_length=100, null=True)),
                ('lat_decimal', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('long_decimal', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('site2', models.CharField(blank=True, max_length=80, null=True)),
                ('jerarquia', models.CharField(blank=True, max_length=50, null=True)),
                ('jerarquia_modif', models.CharField(blank=True, max_length=50, null=True)),
                ('co', models.CharField(blank=True, max_length=100, null=True)),
                ('co_celular', models.CharField(blank=True, max_length=100, null=True)),
                ('co_email', models.CharField(blank=True, max_length=100, null=True)),
                ('coord', models.CharField(blank=True, max_length=100, null=True)),
                ('coord_celular', models.CharField(blank=True, max_length=50, null=True)),
                ('coord_email', models.CharField(blank=True, max_length=100, null=True)),
                ('manager', models.CharField(blank=True, max_length=100, null=True)),
                ('manager_celular', models.CharField(blank=True, max_length=50, null=True)),
                ('manager_email', models.CharField(blank=True, max_length=100, null=True)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('director_celular', models.CharField(blank=True, max_length=50, null=True)),
                ('director_email', models.CharField(blank=True, max_length=100, null=True)),
                ('coordination', models.CharField(blank=True, max_length=50, null=True)),
                ('management', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=20, null=True)),
                ('region_num', models.CharField(blank=True, max_length=4, null=True)),
                ('mercado_ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('mercado_anterior', models.CharField(blank=True, max_length=100, null=True)),
                ('prioridad', models.CharField(blank=True, max_length=4, null=True)),
                ('tipo_ante', models.CharField(blank=True, max_length=50, null=True)),
                ('capacidad_gen', models.CharField(blank=True, max_length=20, null=True)),
                ('cobertura_min', models.CharField(blank=True, max_length=100, null=True)),
                ('acceso', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('municipality', models.CharField(blank=True, max_length=100, null=True)),
                ('state_name', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_modif', models.DateField(auto_now=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('capturado_por', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mopslog',
            name='site_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mantenimiento.Sitio'),
        ),
        migrations.AddField(
            model_name='mops',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mantenimiento.Sitio'),
        ),
    ]
