# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from PortalUV.apps.ingreso.forms import LoginForm
from django.contrib.auth import login,logout, authenticate
from django.http import HttpResponseRedirect
#from PortalUV.backends import UvAuth
def index_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('acceso')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['matricula']
				password = form.cleaned_data['password']
				alumno = authenticate(username=username,password=password)
				if alumno is not None:
					login(request,alumno)
					return HttpResponseRedirect('acceso')
				else:
					mensaje = "error"
		form = LoginForm();
		ctx = {'form': form, 'mensaje': mensaje}
		return render_to_response('index.html',ctx,context_instance=RequestContext(request))

def salir_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def acceso_view(request):
	return render_to_response('acceso.html',context_instance=RequestContext(request))

