"""
URL configuration for clinicadelgado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.contrib import admin
#from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
#from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gestion.urls')),   
    path('',include('users.urls')),
   # path('reset/password_reset',password_reset,{'template_name':'users/password_reset_form.html','email_template_name':'users/password_reset_email.html'},name='password_reset'),

   # path('reset/password_reset_done',password_reset_done,{'template_name':'users/password_reset_done.html'},name='password_reset_done'),
    
    #path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',password_reset_confirm,{'template_name':'users/password_reset_confirm.html'},name='password_reset_confirm'),
   
    #path('reset/done',password_reset_complete, {'template_name':'users/password_reset_complete.html'},name='password_reset_complete'),

    #path('accounts/',include('users.urls',namespace='users')),
    #path('',HomeView.as_view(),name="home")  
]  

#if settings.DEBUG:
 #    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  #   urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   