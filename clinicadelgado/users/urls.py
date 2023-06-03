from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns =[
    path('',views.inicio,name='inicio'),
    path('login/',views.login_user,name='login'),
    path('registro/',views.register_user,name='registro'),
    path('logout/',views.sign_out,name='logout'),

]+static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
