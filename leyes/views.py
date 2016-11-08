from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import(
	CreateView,
	UpdateView,
	DeleteView

)

from .models import Iniciativa


class IniciativaList(ListView):
	model = Iniciativa
	#context_object_name = 'iniciativa'

class IniciativaDetail(DetailView):
	model =  Iniciativa

class IniciativaCreation(CreateView):
	model = Iniciativa
	success_url = reverse_lazy('iniciativa:list')
	fields = ['num', 'nombre', 'turno', 'comision', 'resolutivos', 'enlace','diputado']


class IniciativaUpdate(UpdateView):
	model = Iniciativa
	success_url = reverse_lazy('iniciativa:list')
	fields = ['num', 'nombre', 'turno', 'comision', 'resolutivos', 'enlace','diputado']

class IniciativaDelete(DeleteView):
	model = Iniciativa
	success_url = reverse_lazy('iniciativa:list')
