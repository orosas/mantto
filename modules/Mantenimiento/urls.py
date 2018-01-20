from django.conf.urls import url
from .views import Index, Busqueda, Login, Detalle_Sitio, Preventivos, Preventivoform, Correctivos

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^(?P<error>[\w-]+)$', Index, name='index-disclaimer'),
    url(r'^$', Index, name='index'),
    url(r'^busqueda/$', Busqueda, name='busqueda'),
    url(r'^preventivos/$', Preventivos, name='preventivos'),
    url(r'^preventivoform/$', Preventivoform, name='preventivoform'),
    url(r'^correctivos/$', Correctivos, name='correctivos'),
    url(r'^login$', Login, name='login'),
    url(r'^detallesitio/(?P<pk>\d+)/$', Detalle_Sitio, name='detalle_sitio'),
    #url(r'^region/(?P<region>[\w-]+)/$', lista_Sitiosxregion, name='sitios_por_region'),
    #url(r'^busqueda/$', Busqueda_Sitio, name='busqueda_sitio'),
    #url(r'^detallesitio/(?P<pk>\d+)/$', Detalle_Sitio, name='detalle_sitio'),
]
