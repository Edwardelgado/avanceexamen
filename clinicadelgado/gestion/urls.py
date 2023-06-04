from django.urls import path, include
from . import views
from .views import DoctorList, gestion, login,registro, DoctorDetail, DoctorUpdate, DoctorCreate, DoctorDelete
from .views import EspecialidadList, EspecialidadDetail, EspecialidadUpdate, EspecialidadCreate, EspecialidadDelete
from .views import TiposeguroList, TiposeguroDetail, TiposeguroUpdate, TiposeguroCreate, TiposeguroDelete
from .views import TipodocumentoList, TipodocumentoDetail, TipodocumentoUpdate, TipodocumentoCreate, TipodocumentoDelete
from .views import PacienteList, PacienteDetail, PacienteUpdate, PacienteCreate, PacienteDelete
from .views import CitaList, CitaDetail, CitaUpdate, CitaCreate, CitaDelete



urlpatterns = [
    path('gestion/',gestion,name='gestion'),
    path('login/',login,name='login'),
    path('registro/',registro,name='registro'),
   

    path('gestion/doctores/',DoctorList.as_view(),name='doctores'),
    path('gestion/doctor/<int:pk>/',DoctorDetail.as_view(),name='doctor'),
    path('gestion/doctor/create/',DoctorCreate.as_view(),name='doctor-create'),
    path('gestion/doctor/update/<int:pk>/',DoctorUpdate.as_view(),name='doctor-update'),
    #path('doctor/delete/<int:pk>/',DoctorDelete.as_view(),name='doctor-delete'),
    path('gestion/doctor/delete/<int:pk>',views.eliminar_doctor,name='eliminar_doctor'),

    path('gestion/especialidades/',EspecialidadList.as_view(),name='especialidades'),
    path('gestion/especialidad/<int:pk>/',EspecialidadDetail.as_view(),name='especialidad'),
    path('gestion/especialidad/create/',EspecialidadCreate.as_view(),name='especialidad-create'),
    path('gestion/especialidad/update/<int:pk>/',EspecialidadUpdate.as_view(),name='especialidad-update'),
    #path('gestion/especialidad/delete/<int:pk>/',EspecialidadDelete.as_view(),name='especialidad-delete'),
    path('gestion/especialidad/delete/<int:pk>/',views.eliminar_especialidad,name='eliminar_especialidad'),
  
    path('gestion/tiposeguros/',TiposeguroList.as_view(),name='tiposeguros'),
    path('gestion/tiposeguro/<int:pk>/',TiposeguroDetail.as_view(),name='tiposeguro'),
    path('gestion/tiposeguro/create/',TiposeguroCreate.as_view(),name='tiposeguro-create'),
    path('gestion/tiposeguro/update/<int:pk>/',TiposeguroUpdate.as_view(),name='tiposeguro-update'),
    #path('gestion/tiposeguro/delete/<int:pk>/',TiposeguroDelete.as_view(),name='tiposeguro-delete'),
    path('gestion/tiposeguro/delete/<int:pk>/',views.eliminar_tiposeguro,name='eliminar_tiposeguro'),

    path('gestion/tipodocumentos/',TipodocumentoList.as_view(),name='tipodocumentos'),
    path('gestion/tipodocumento/<int:pk>/',TipodocumentoDetail.as_view(),name='tipodocumento'),
    path('gestion/tipodocumento/create/',TipodocumentoCreate.as_view(),name='tipodocumento-create'),
    path('gestion/tipodocumento/update/<int:pk>/',TipodocumentoUpdate.as_view(),name='tipodocumento-update'),
    #path('gestion/tipodocumento/delete/<int:pk>/',TipodocumentoDelete.as_view(),name='tipodocumento-delete'),
    path('gestion/tipodocumento/delete/<int:pk>/',views.eliminar_tipodocumento,name='eliminar_tipodocumento'),

    path('gestion/pacientes/',PacienteList.as_view(),name='pacientes'),
    path('gestion/paciente/<int:pk>/',PacienteDetail.as_view(),name='paciente'),
    path('gestion/paciente/create/',PacienteCreate.as_view(),name='paciente-create'),
    path('gestion/paciente/update/<int:pk>/',PacienteUpdate.as_view(),name='paciente-update'),
    #path('gestion/paciente/delete/<int:pk>/',PacienteDelete.as_view(),name='paciente-delete'),
    path('gestion/paciente/delete/<int:pk>/',views.eliminar_paciente,name='eliminar_paciente'),

    path('gestion/citas/',CitaList.as_view(),name='citas'),
    path('gestion/cita/<int:pk>/',CitaDetail.as_view(),name='cita'),
    path('gestion/cita/create/',CitaCreate.as_view(),name='cita-create'),
    path('gestion/cita/update/<int:pk>/',CitaUpdate.as_view(),name='cita-update'),
    #path('gestion/cita/delete/<int:pk>/',CitaDelete.as_view(),name='cita-delete'),
    path('gestion/cita/delete/<int:pk>/',views.eliminar_cita,name='eliminar_cita'),

    
]