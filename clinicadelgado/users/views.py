from .forms import EditProfileForm
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Usuario
from django.core.paginator import Paginator
from .forms import LoginForm, RegisterForm, ResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User =get_user_model()
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def login_user(request):
    form = LoginForm()
    message=''
   
    if request.method=='POST':    
        form = LoginForm(request.POST)  
        if form.is_valid():
            print('Metodo:', request.method)
            cd = form.cleaned_data #recupera la data limpia
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    message = f'Hola {user.username}!! Te has logueado'
                    return render(request,'gestion/inicio.html',{'user:': user})
                    #return render(request,'base2.html',{'user:': user})
                else:
                    message = 'El usuario ingresado no se encuentra activo'
            else:
                message = 'Cuenta inválida'


    return render(request,'users/login.html', context={'form': form, 'messages': message}) 
    #return render(request,'gestion/inicio.html', context={'form': form, 'messages': message})    


def register_user(request):
    if request.method =='GET':
        form = RegisterForm()
        return render(request, 'users/registro.html',{'form':form})
    
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'Te has logeado correctamente')
            login(request,user)
            return redirect('inicio')
        else:
            return render(request, 'users/registro.html',{'form':form})


def sign_out(request):
    logout(request)
    messages.success(request,f'Acabas de cerrar tu sesion')
    return redirect('inicio')

#usuarios
class UsuarioList(ListView):
    model = Usuario
    context_object_name = 'usuarios'

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['username','full_name','email','telefono']
    success_url = reverse_lazy('usuarios')
    
    def form_valid(self, form):
        messages.success(self.request, "Los datos del usuario fue actualizado correctamente.")
        return super(UsuarioUpdate,self).form_valid(form)



def eliminar_usuario(request,pk):
 usuario =Usuario.objects.get(username=pk)
 usuario.delete()
 return redirect('usuarios')

@login_required
def EditProfile(request):
    user = request.user.id
    usuario = Usuario.objects.get(user__id=user)
    user_basic_info = User.objects.get(id=user)

    if request.method == 'POST':
        form=EditProfileForm(request.POST,instance=usuario)
        if form.is_valid():
            usuario.full_name =form.cleaned_data.get('full_name')
            usuario.direccion =form.cleaned_data.get('direccion')
            usuario.telefono =form.cleaned_data.get('telefono')

            usuario.save()
            return redirect('usuarios', username=request.user.username)
    else:
        form = EditProfileForm(instance=usuario)
    
    context={
        'form':form,
    }
    return render(request,'users/edit.html', context)