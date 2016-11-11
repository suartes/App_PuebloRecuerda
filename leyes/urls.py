from django.conf.urls import url
from .views import index, iniciativa_view,iniciativa_list,iniciativa_edit,iniciativa_delete

urlpatterns = (
   url(r'^leyes/$',index,name='index'),
   url(r'^leyes/nuevo/$',iniciativa_view, name="iniciativa_crear"),
   url(r'^leyes/listar/$',iniciativa_list, name="iniciativa_listar"),
   url(r'^leyes/editar/(?P<id_iniciativa>\d+)$',iniciativa_edit, name="iniciativa_editar"),
   url(r'^leyes/eliminar/(?P<id_iniciativa>\d+)$', iniciativa_delete, name="iniciativa_eliminar"),

   )


