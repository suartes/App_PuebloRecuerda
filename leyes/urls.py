from django.conf.urls import url
from .views import index, iniciativa_view

urlpatterns = (
   url(r'^leyes/$',index,name='index'),
   url(r'^leyes/nuevo/$',iniciativa_view, name="iniciativa_crear"),
    #url(r'^leyes/nuevo$', IniciativaCreation.as_view(), name="iniciativa_new"),
    #url(r'^leyes/editar/(?P<pk>\d+)$', IniciativaUpdate.as_view(), name="iniciativa_update"),
    #url(r'^leyes/borrar/(?P<pk>\d+)$', IniciativaDelete.as_view(), name="iniciativa_delete"),
)
