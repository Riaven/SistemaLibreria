from django.conf.urls import url
from apps.producto.views import index, producto_view, producto_list, producto_edit, producto_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', producto_view, name='producto_crear'),
    url(r'^listar$', producto_list, name='producto_listar'),
    url(r'^editar/(?P<id_producto>\d+)/$', producto_edit, name='producto_editar'),
    url(r'^eliminar/(?P<id_producto>\d+)/$', producto_delete, name='producto_eliminar'),
]