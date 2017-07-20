from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Candidatos
from apps.tipos.categoria_eleccion.models import Categoria
from apps.tipos.tipo_eleccion.models import Tipo_eleccion
from apps.partidos.models import Partidos
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.circuitos.models import Circuito
from .forms import CandidatosForm
from apps.elecciones.models import Eleccion
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from apps.exitpoll.models import ExitPoll
import base64
from PIL import Image
import StringIO
from django.conf import settings


@login_required(login_url='/')
def RegistrarCandidatos(request):
    """ Vista basada en Metodos o funciones: (`Registrar`)"""
    list_partidos = Partidos.objects.all()
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        existe = Candidatos.objects.filter(cedula=cedula).exists()
        if existe:
            return HttpResponse('existe')
        else:
            form_reg_candidato = CandidatosForm(request.POST, request.FILES)
            if form_reg_candidato.is_valid():
                new_reg_candidato = form_reg_candidato.save(commit=False)

                nombre = request.FILES['foto'].name
                extension = nombre.split(".")[-1]
                ruta_image = settings.MEDIA_ROOT
                
                archivo = ruta_image+'/foto_candidato/'+str(cedula+'.'+extension)
                img = Image.open(form_reg_candidato.cleaned_data['foto'])
                img.resize((94, 124), Image.ANTIALIAS)
                foto_save = 'foto_candidato/'+str(cedula+'.'+extension)
                
                img.save(archivo)
                image = open(archivo) 
                fot_c =  image.read()
                fot_bina_c = base64.encodestring(fot_c) #Codifica en formato Binario
                new_reg_candidato.foto_binario = fot_bina_c #Indica en que campo se guardara
                new_reg_candidato.foto = foto_save
                

                new_reg_candidato.save()
                
            return HttpResponseRedirect('/candidatos/')
    else:
        form_reg_candidato = CandidatosForm()
    ctx = {'form_reg_candidato': form_reg_candidato, 'list_partidos': list_partidos}
    return render_to_response('candidato/candidato.html',
                              ctx, context_instance=RequestContext(request))


@login_required(login_url='/')
def EditarCandidatos(request, pk):
    """ Vista basada en Metodos o funciones: (`modificar`)"""
    obj_reg_can = Candidatos.objects.get(id=pk)
    # print obj_reg_can.foto
    list_partido = Partidos.objects.all()
    cedula = request.POST.get('cedula')
    if request.method == 'POST':
        obj_reg_edit_cen = CandidatosForm(request.POST, request.FILES, instance=obj_reg_can)

        if obj_reg_edit_cen.is_valid():
            img_val = request.FILES.get('foto')
            if img_val is None:
                new_reg_candidato = obj_reg_edit_cen.save(commit=False)
                new_reg_candidato.save()
            else:
                new_reg_candidato = obj_reg_edit_cen.save(commit=False)
                nombre = request.FILES['foto'].name
                extension = nombre.split(".")[-1]
                ruta_image = settings.MEDIA_ROOT
    
                archivo = ruta_image+'/foto_candidato/'+str(cedula+'.'+extension)
                img = Image.open(obj_reg_edit_cen.cleaned_data['foto'])
                img.resize((94, 124), Image.ANTIALIAS)
                foto_save = 'foto_candidato/'+str(cedula+'.'+extension)
                
                img.save(archivo)
                image = open(archivo) 
                fot_c =  image.read()
                fot_bina_c = base64.encodestring(fot_c) #Codifica en formato Binario
                new_reg_candidato.foto_binario = fot_bina_c #Indica en que campo se guardara
                new_reg_candidato.foto = foto_save

                new_reg_candidato.save()
                
            return HttpResponseRedirect('/candidatos/')
    else:
        obj_reg_edit_cen = CandidatosForm(instance=obj_reg_can)
    ctx = {'obj_reg_edit_cen': obj_reg_edit_cen, 'obj_reg_can': obj_reg_can,
           'list_partido': list_partido}
    return render_to_response('candidato/modificar.html', ctx,
                              context_instance=RequestContext(request))


class ListarCandidatos(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Candidatos
    template_name = 'candidato/listar.html'
    context_object_name = "listar_candidato"
    
    def post(self, request, *args, **kwargs):

        pk_usuario = self.request.POST.get('pk')
        status = self.request.POST.get('status')

        #Validamos el status
        if status == 'false':
            status = False
        else:
            status = True

        #Buscamos el id(pk) del usuario en el modelo de Usuario
        eleccion = Candidatos.objects.filter(id=pk_usuario)
        eleccion.update(
            candidato_activo=status
        )
        return HttpResponse('exito')


class BorrarCandidatos(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
         satisfactoriamente.
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Candidatos
    template_name = 'candidato/borrar.html'
    context_object_name = "borrar_candidato"
    success_url = reverse_lazy("listar_candidato")

    def get_context_data(self, **kwargs):
        context = super(BorrarCandidatos, self).get_context_data(**kwargs)
        id_cand = self.kwargs['pk']
        ele = ExitPoll.objects.all()
        existe = ele.filter(candidatos_id=id_cand)
        cantidad = len(existe)

        context['cantidad'] = cantidad
        return context
