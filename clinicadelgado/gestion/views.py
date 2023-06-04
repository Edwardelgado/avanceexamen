from typing import Any, Dict
from urllib import request
from django import forms
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Cita, Doctor, Especialidad, Paciente, Tipodocumento, Tiposeguro, Usuario
from django.core.paginator import Paginator

def gestion(request):
    return render(request,'gestion/inicio.html')
def login(request):
    return render(request,'login/')

def registro(request):
    return render(request,'registro/')


#doctor
class DoctorList(ListView):
    model = Doctor
    context_object_name = 'doctores'
   # page = request.GET.get('page', 1)
    #try:
     #   paginator = Paginator(doctores, 5)

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
        messages.success(self.request, "Los datos del doctor fue actualizado correctamente.")
        return super(DoctorUpdate,self).form_valid(form)
    
class DoctorDelete(DeleteView):
    model = Doctor
    template_name="gestion/doctor_delete.html"
    success_url = reverse_lazy('erp:doctores')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de un doctor'
        context['entity']='doctor'
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
        context['entity']='especialidad'
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
        context['entity']='tiposeguro'
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
        context['entity']='tipodocumento'
        context['list_url']=reverse_lazy('erp:tipodocumentos')
        return context
    
  
#paciente
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class PacienteList(ListView):
    model = Paciente
    context_object_name = 'pacientes'

class PacienteDetail(DetailView):
    model = Paciente
    context_object_name = 'paciente'

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['tipo_documento','nro_documento','nombres','apellidos','direccion','fecha_nacimiento','tipo_seguro']
    success_url = reverse_lazy('pacientes')
    
   
    def form_valid(self, form):
        
        widgets = {
            
            'fecha_nacimiento': DateTimeInput(attrs={'class': 'form-control'}),
            
        }
        form.instance.user = self.request.user
        messages.success(self.request, "El Paciente fue creado correctamente.")
        return super(PacienteCreate,self).form_valid(form)
    
class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['tipo_documento','nro_documento','nombres','apellidos','direccion','fecha_nacimiento','tipo_seguro']
    success_url = reverse_lazy('pacientes')
    
    def form_valid(self, form):
        messages.success(self.request, "El paciente fue actualizado correctamente.")
        return super(PacienteUpdate,self).form_valid(form)
    
class PacienteDelete(DeleteView):
    model = Paciente
    template_name="gestion/paciente_delete.html"
    success_url = reverse_lazy('erp:pacientes')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de un paciente'
        context['entity']='paciente'
        context['list_url']=reverse_lazy('erp:pacientes')
        return context
    
  
def eliminar_doctor(request,pk):
 doctor =Doctor.objects.get(doctor_id=pk)
 doctor.delete()
 return redirect('doctores')

def eliminar_especialidad(request,pk):
 especialidad =Especialidad.objects.get(especialidad_id=pk)
 especialidad.delete()
 return redirect('especialidades')
  
def eliminar_tipodocumento(request,pk):
 tipodocumento =Tipodocumento.objects.get(tipo_documento_id=pk)
 tipodocumento.delete()
 return redirect('tipodocumentos')
  
def eliminar_tiposeguro(request,pk):
 tiposeguro =Tiposeguro.objects.get(tipo_seguro_id=pk)
 tiposeguro.delete()
 return redirect('tiposeguros')

def eliminar_paciente(request,pk):
 paciente =Paciente.objects.get(paciente_id=pk)
 paciente.delete()
 return redirect('pacientes')



#cita

class CitaList(ListView):
    model = Cita
    context_object_name = 'citas'

class CitaDetail(DetailView):
    model = Cita
    context_object_name = 'cita'

class CitaCreate(CreateView):
    model = Cita
    fields = ['paciente','fecha_cita','especialidad','doctor','observaciones','username']
    success_url = reverse_lazy('citas')
    
   
    def form_valid(self, form):
        
        widgets = {
            
            'fecha_cita': DateTimeInput(attrs={'class': 'form-control'}),
            
        }
        form.instance.user = self.request.user
        messages.success(self.request, "La cita fue creada correctamente.")
        return super(CitaCreate,self).form_valid(form)
    
class CitaUpdate(UpdateView):
    model = Cita
    fields = ['paciente','fecha_cita','especialidad','doctor','observaciones','username']
    success_url = reverse_lazy('citas')
    
    def form_valid(self, form):
        messages.success(self.request, "La cita fue actualizada correctamente.")
        return super(CitaUpdate,self).form_valid(form)
    
class CitaDelete(DeleteView):
    model = Cita
    template_name="gestion/cita_delete.html"
    success_url = reverse_lazy('erp:citas')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de una cita'
        context['entity']='cita'
        context['list_url']=reverse_lazy('erp:citas')
        return context

def eliminar_cita(request,pk):
 cita =Cita.objects.get(cita_id=pk)
 cita.delete()
 return redirect('citas')
  
  
  