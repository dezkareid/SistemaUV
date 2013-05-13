from django.conf.urls import patterns,url

urlpatterns = patterns('PortalUV.apps.ingreso.views',
	url(r'^$', 'index_view', name='index'),
	url(r'^acceso/$', 'acceso_view', name='acceso'),
	url(r'^salir$', 'salir_view', name='salir'),
)