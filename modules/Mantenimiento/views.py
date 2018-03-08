from django.shortcuts import render
from django.db.models import Q
from .forms import BusquedaForm
from .models import Sitio, Mops

#from django.http import HttpResponse

# Create your views here.
def Index(request):

	if request.user.is_authenticated():
		form = BusquedaForm()
		return render(request, 'Mantenimiento/index.html',{'form': form, })
	else:
		return render(request, 'Mantenimiento/login.html',)
	#return render(request, 'Mantenimiento/index.html',)

	#return HttpResponse('Dentro de función Index')
	'''
	if request.user.is_authenticated():
		form = BusquedaForm()
		return render(request, 'Mantenimiento/index.html', {'form': form})
	else:
		return render(request, 'Mantenimiento/login.html',)
	'''

def Busqueda(request):

	if request.method == 'POST':
		form = BusquedaForm(request.POST)
		if form.is_valid():
			q = form.cleaned_data['q']

			sitios = Sitio.objects.filter(Q(site__unaccent__icontains=q)|
											Q(site_name__unaccent__icontains=q)|
											Q(iden__icontains=q)|
											Q(gsm__icontains=q)|
											Q(id_3g__icontains=q)|
											Q(lte__icontains=q)|
											Q(lte__icontains=q)

								)

			return render(request, 'Mantenimiento/index.html', {'sitios':sitios, 'form': form})

		else:
			elerror = True
			return redirect('Mantenimiento:index-disclaimer', elerror)
	else:
		form = BusquedaForm()
		return render(request, 'Disclaimer/index_disclaimer.html', {'form': form})
	pass



def Login(request):
	pass



def Detalle_Sitio(request,pk):
	sitio = Sitio.objects.get(pk=pk)
	mops = sitio.mops_set.all()

	print("dentro Detalle_Sitio pk "+pk)
	#status = Status.objects.get(pk=pk)
	#mantenimiento = Mantenimiento.objects.get(pk=pk)

	print("sitio NAME: " + str(sitio.site_name))

	form = BusquedaForm()

	return render(request,'Mantenimiento/detallesitio_disclaimer.html', {'sitio': sitio,
																		'form': form,
																		'mops': mops,
																		}
					)


def Preventivos(request):
	form = BusquedaForm()
	return render(request, 'Mantenimiento/preventivos.html', {'form': form})



def Preventivoform(request):
	form = BusquedaForm()
	return render(request, 'Mantenimiento/preventivoform.html', {'form': form})


def Correctivos(request):
	form = BusquedaForm()
	return render(request, 'Mantenimiento/correctivos.html', {'form': form})
