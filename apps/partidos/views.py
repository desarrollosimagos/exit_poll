from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from apps.candidatos.models import Candidatos
from .models import Partidos
from django.contrib.auth.decorators import login_required  # impedir el acceso al sistema
from django.core import serializers
from .forms import PartidosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import base64
from PIL import Image
import StringIO
from django.conf import settings


@login_required(login_url='/')
def RegistrarPartidos(request):
    """ Vista basada en Metodos o funciones: (`Registrar`). """

    if request.method == 'POST':
        n_partidos = request.POST.get('n_partidos')
        existe = Partidos.objects.filter(n_partidos=n_partidos).exists()
        if existe:
            return HttpResponse('existe')

        else:
            form_reg_par = PartidosForm(request.POST, request.FILES)
        if form_reg_par.is_valid():
            new_reg_par = form_reg_par.save(commit=False)
            nombre = request.FILES['foto_partido'].name
            extension = nombre.split(".")[-1]
            ruta_image = settings.MEDIA_ROOT

            archivo = ruta_image+'/logo_partidos/'+str(n_partidos+'.'+extension)
            img = Image.open(form_reg_par.cleaned_data['foto_partido'])
            img.resize((94, 124), Image.ANTIALIAS)
            foto_save = 'logo_partidos/'+str(n_partidos+'.'+extension)

            img.save(archivo)
            image = open(archivo)
            fot_c = image.read()
            fot_bina_c = base64.encodestring(fot_c) #Codifica en formato Binario
            new_reg_par.partido_binario = fot_bina_c #Indica en que campo se guardara
            new_reg_par.foto = foto_save

            new_reg_par.save()

        return HttpResponseRedirect('/partidos/')
    else:
        form_reg_par = PartidosForm()
    ctx = {'form_reg_par': form_reg_par}  # ctx = Contexto

    return render_to_response('partido/partido.html',
                              ctx, context_instance=RequestContext(request))


@login_required(login_url='/')
def EditarPartidos(request, pk):
    """ Vista basada en Metodos o funciones: (`Modificar`)."""
    obj_reg_part = Partidos.objects.get(id=pk)
    n_partidos = request.POST.get('n_partidos')

    if request.method == 'POST':
        form_reg_parr = PartidosForm(request.POST, request.FILES, instance=obj_reg_part)

        if form_reg_parr.is_valid():
            img_val = request.FILES.get('foto_partido')
            if img_val is None:
                edit_reg_parr = form_reg_parr.save(commit=False)
                edit_reg_parr.save()
            else:
                edit_reg_parr = form_reg_parr.save(commit=False)
                nombre = request.FILES['foto_partido'].name
                extension = nombre.split(".")[-1]
                ruta_image = settings.MEDIA_ROOT
    
                archivo = ruta_image+'/logo_partidos/'+str(n_partidos+'.'+extension)
                img = Image.open(form_reg_parr.cleaned_data['foto_partido'])
                img.resize((94, 124), Image.ANTIALIAS)
                foto_save = 'logo_partidos/'+str(n_partidos+'.'+extension)
    
                img.save(archivo)
                image = open(archivo) 
                fot_c = image.read()
                fot_bina_c = base64.encodestring(fot_c) #Codifica en formato Binario
                edit_reg_parr.partido_binario = fot_bina_c #Indica en que campo se guardara
                edit_reg_parr.foto = foto_save
    
                edit_reg_parr.save()

            return HttpResponseRedirect('/partidos/')
    else:
        form_reg_parr = PartidosForm(instance=obj_reg_part)
    ctx = {'form_reg_parr': form_reg_parr, 'obj_reg_part': obj_reg_part}  # ctx = Contexto
    return render_to_response('partido/modificar.html',
                              ctx, context_instance=RequestContext(request))


class ListarPartidos(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    
    """
    model = Partidos
    template_name = 'partido/listar.html'
    context_object_name = "listar_partido"


class BorrarPartidos(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
                            satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Partidos
    template_name = 'partido/borrar.html'
    context_object_name = "borrar_partido"
    success_url = reverse_lazy("listar_partido")
    
    def get_context_data(self, **kwargs):
        context = super(BorrarPartidos, self).get_context_data(**kwargs)
        id_par = self.kwargs['pk']
        candi = Candidatos.objects.all()
        existe = candi.filter(part_politico_id=id_par)
        cantidad = len(existe)
        
        context['cantidad'] = cantidad
        return context

