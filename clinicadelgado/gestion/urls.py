from django.urls import path, include
from .views import DoctorList, inicio, DoctorDetail, DoctorUpdate, DoctorCreate, DoctorDelete
from .views import EspecialidadList, EspecialidadDetail, EspecialidadUpdate, EspecialidadCreate, EspecialidadDelete
from .views import TiposeguroList, TiposeguroDetail, TiposeguroUpdate, TiposeguroCreate, TiposeguroDelete
from .views import TipodocumentoList, TipodocumentoDetail, TipodocumentoUpdate, TipodocumentoCreate, TipodocumentoDelete


urlpatterns = [
    path('',inicio,name='inicio'),
    path('doctores/',DoctorList.as_view(),name='doctores'),
    path('doctor/<int:pk>/',DoctorDetail.as_view(),name='doctor'),
    path('doctor/create/',DoctorCreate.as_view(),name='doctor-create'),
    path('doctor/update/<int:pk>/',DoctorUpdate.as_view(),name='doctor-update'),
    path('doctor/delete/<int:pk>/',DoctorDelete.as_view(),name='doctor-delete'),

    path('especialidades/',EspecialidadList.as_view(),name='especialidades'),
    path('especialidad/<int:pk>/',EspecialidadDetail.as_view(),name='especialidad'),
    path('especialidad/create/',EspecialidadCreate.as_view(),name='especialidad-create'),
    path('especialidad/update/<int:pk>/',EspecialidadUpdate.as_view(),name='especialidad-update'),
    path('especialidad/delete/<int:pk>/',EspecialidadDelete.as_view(),name='especialidad-delete'),

    path('tiposeguros/',TiposeguroList.as_view(),name='tiposeguros'),
    path('tiposeguro/<int:pk>/',TiposeguroDetail.as_view(),name='tiposeguro'),
    path('tiposeguro/create/',TiposeguroCreate.as_view(),name='tiposeguro-create'),
    path('tiposeguro/update/<int:pk>/',TiposeguroUpdate.as_view(),name='tiposeguro-update'),
    path('tiposeguro/delete/<int:pk>/',TiposeguroDelete.as_view(),name='tiposeguro-delete'),

    path('tipodocumentos/',TipodocumentoList.as_view(),name='tipodocumentos'),
    path('tipodocumento/<int:pk>/',TipodocumentoDetail.as_view(),name='tipodocumento'),
    path('tipodocumento/create/',TipodocumentoCreate.as_view(),name='tipodocumento-create'),
    path('tipodocumento/update/<int:pk>/',TipodocumentoUpdate.as_view(),name='tipodocumento-update'),
    path('tipodocumento/delete/<int:pk>/',TipodocumentoDelete.as_view(),name='tipodocumento-delete'),
    
]