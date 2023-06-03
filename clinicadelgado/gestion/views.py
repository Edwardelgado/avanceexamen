from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Doctor, Especialidad, Tipodocumento, Tiposeguro

def inicio(request):
    return render(request,'inicio.html')


#doctor
class DoctorList(ListView):
    model = Doctor
    context_object_name = 'doctores'

class DoctorDetail(DetailView):
    model = Doctor
    context_object_name = 'doctor'



class DoctorCreate(CreateView):
    model = Doctor
    fields = ['doctor_nombre','doctor_direccion','doctor_telefono']
    success_url = reverse_lazy('doctores')
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El doctor fue creada correctamente.")
        return super(DoctorCreate,self).form_valid(form)
    
class DoctorUpdate(UpdateView):
    model = Doctor
    fields = ['doctor_nombre','doctor_direccion','doctor_telefono']
    success_url = reverse_lazy('doctores')
    
    def form_valid(self, form):
        messages.success(self.request, "La tarea fue actualizada correctamente.")
        return super(DoctorUpdate,self).form_valid(form)
    
class DoctorDelete(DeleteView):
    model = Doctor
    template_name="gestion/doctor_delete.html"
    success_url = reverse_lazy('erp:doctores')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de un doctor'
        context['entity']='Doctor'
        context['list_url']=reverse_lazy('erp:doctores')
        return context

#especialidad
class EspecialidadList(ListView):
    model = Especialidad
    context_object_name = 'especialidades'

class EspecialidadDetail(DetailView):
    model = Especialidad
    context_object_name = 'especialidades'



class EspecialidadCreate(CreateView):
    model = Especialidad
    fields = ['especialidad_nombre']
    success_url = reverse_lazy('especialidades')
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La especialidad fue creada correctamente.")
        return super(EspecialidadCreate,self).form_valid(form)
    
class EspecialidadUpdate(UpdateView):
    model = Especialidad
    fields = ['especialidad_nombre']
    success_url = reverse_lazy('especialidades')
    
    def form_valid(self, form):
        messages.success(self.request, "La especialidad fue actualizada correctamente.")
        return super(EspecialidadUpdate,self).form_valid(form)
    
class EspecialidadDelete(DeleteView):
    model = Especialidad
    template_name="gestion/especialidad_delete.html"
    success_url = reverse_lazy('erp:especialidades')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de una especialidad'
        context['entity']='Especialidad'
        context['list_url']=reverse_lazy('erp:especialidades')
        return context
    

#tipo seguro
class TiposeguroList(ListView):
    model = Tiposeguro
    context_object_name = 'tiposeguros'

class TiposeguroDetail(DetailView):
    model = Tiposeguro
    context_object_name = 'tiposeguro'

class TiposeguroCreate(CreateView):
    model = Tiposeguro
    fields = ['tipo_seguro_nombre']
    success_url = reverse_lazy('tiposeguros')
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El tipo de seguro fue creado correctamente.")
        return super(TiposeguroCreate,self).form_valid(form)
    
class TiposeguroUpdate(UpdateView):
    model = Tiposeguro
    fields = ['tipo_seguro_nombre']
    success_url = reverse_lazy('tiposeguros')
    
    def form_valid(self, form):
        messages.success(self.request, "El tipo de seguro fue actualizado correctamente.")
        return super(TiposeguroUpdate,self).form_valid(form)
    
class TiposeguroDelete(DeleteView):
    model = Tiposeguro
    template_name="gestion/tiposeguro_delete.html"
    success_url = reverse_lazy('erp:tiposeguros')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de un tipo de seguro'
        context['entity']='Especialidad'
        context['list_url']=reverse_lazy('erp:tiposeguros')
        return context
    
  
#tipo documento
class TipodocumentoList(ListView):
    model = Tipodocumento
    context_object_name = 'tipodocumentos'

class TipodocumentoDetail(DetailView):
    model = Tipodocumento
    context_object_name = 'tipodocumento'

class TipodocumentoCreate(CreateView):
    model = Tipodocumento
    fields = ['tipo_documento_nombre']
    success_url = reverse_lazy('tipodocumentos')
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El tipo de documento fue creado correctamente.")
        return super(TipodocumentoCreate,self).form_valid(form)
    
class TipodocumentoUpdate(UpdateView):
    model = Tipodocumento
    fields = ['tipo_documento_nombre']
    success_url = reverse_lazy('tipodocumentos')
    
    def form_valid(self, form):
        messages.success(self.request, "El tipo de documento fue actualizado correctamente.")
        return super(TipodocumentoUpdate,self).form_valid(form)
    
class TipodocumentoDelete(DeleteView):
    model = Tipodocumento
    template_name="gestion/tipodocumento_delete.html"
    success_url = reverse_lazy('erp:tipodocumentos')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de un tipo de documentos'
        context['entity']='Tipodocumento'
        context['list_url']=reverse_lazy('erp:tipodocumentos')
        return context
    
  
    
  
  