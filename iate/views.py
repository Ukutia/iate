from cgitb import html

from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .plantillas import evaluar
from .forms import CreateUserForm




@login_required(login_url='login')
def inicio(request): # Funcion Vista / request siempre como primer parametro 
    texto = evaluar("base.txt")
    messages.info(request, texto)

    return render(request, 'iatehome.html')
    
def paginaRegistro(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Cuenta Creada para: ' + user)
    context = {'form':form}      
    return render(request, 'registration/registro.html',context) 
    

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('inicio')
        else:
            messages.info(request, 'El nombre de Usuario o la Contraseña es incorrecto')
            

    context = {}
    return render(request, 'registration/login.html', context)


def salir(request):
    logout(request)
    return redirect('login')


