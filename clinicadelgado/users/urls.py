from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import UsuarioList, UsuarioUpdate, EditProfile

#app_name="accounts"

urlpatterns =[
    path('',views.inicio,name='inicio'),
    path('users/login/',views.login_user,name='login'),
    path('users/registro/',views.register_user,name='registro'),
    path('users/logout/',views.sign_out,name='logout'),

    #path('users/Reset/',views.password_reset,name='password_reset'),

    path('users/',UsuarioList.as_view(),name='usuarios'),
    #path('<username>/edit',EditProfile,name='usuario-update')
    path('users/update/<str:pk>',UsuarioUpdate.as_view(),name='usuario-update'),
    path('users/delete/<str:pk>',views.eliminar_usuario,name='eliminar_usuario'),

]+static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
