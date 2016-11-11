#from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
#from django.http import HttpResponse

from .models import Iniciativa
from .forms import IniciativaForm

def index(request):
    return render(request,'leyes/index.html')

def iniciativa_view(request):
	if request.method == 'POST':
		form=IniciativaForm(request.POST)
		if form.is_valid():
				form.save()
		return redirect('leyes:index')
	else:
		form=IniciativaForm()

	return render(request,'leyes/iniciativa_form.html',{'form':form})


def iniciativa_list(request):
	iniciativa = Iniciativa.objects.all().order_by('id')
	contexto = {'iniciativas':iniciativa}
	return render(request, 'leyes/iniciativa_list.html', contexto)

def iniciativa_edit(request, id_iniciativa):
	iniciativa = Iniciativa.objects.get(id=id_iniciativa)
	if request.method == 'GET':
		form = IniciativaForm(instance=iniciativa)
	else:
		form = IniciativaForm(request.POST, instance=iniciativa)
		if form.is_valid():
			form.save()
		return redirect('leyes:iniciativa_listar')
	return render(request, 'leyes/iniciativa_form.html', {'form':form})

def iniciativa_delete(request, id_iniciativa):
	iniciativa = Iniciativa.objects.get(id=id_iniciativa)
	if request.method == 'POST':
		iniciativa.delete()
		return redirect('leyes:iniciativa_listar')
	return render(request, 'leyes/iniciativa_delete.html', {'iniciativa':iniciativa})


"""class IniciativaList(ListView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_list')
	#context_object_name = 'leyes'

class IniciativaDetail(DetailView):
	model =  Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_detail')

class IniciativaCreation(CreateView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_create')
	fields = ['num', 'nombre', 'turno', 'comision', 'resolutivos', 'enlace','diputado']

class IniciativaUpdate(UpdateView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:iniciativa_update')
	fields = ['num', 'nombre', 'turno', 'comision', 'resolutivos', 'enlace','diputado']

class IniciativaDelete(DeleteView):
	model = Iniciativa
	success_url = reverse_lazy('leyes:delete')"""