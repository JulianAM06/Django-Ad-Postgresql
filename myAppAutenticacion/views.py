from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm



#class VRegistro(View):
    
    #def get(self, request):
        #form=UserCreationForm()
        #return render (request, 'registro.html', {'form':form})
    
    #def post(self, request):
        #form=UserCreationForm(request.POST)
        
        #if form.is_valid():
        
            #usuario = form.save()
            
            #login(request, usuario)
            
            #return redirect('/tienda/')
        
        #else:
                
            #return render (request, 'error.html')
        
def cerrar_sesion(request):
    
    logout(request)
    
    return redirect('/')

def iniciar (request):
    
    if request.method=='POST':
        
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contra)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('/')
                
            else:
                return render (request, 'error2.html')
            
        else:
            
            return render (request, 'error2.html')
                

    form=AuthenticationForm()
    
    return render (request, 'login.html', {'form':form})


#Nuevo Formulario para adicionar mas campos

def register (request):
    
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            
            login (request, user)
            
            return redirect ('/')
        
        else:
                
            return render (request, 'error.html')
    
    return render (request, 'registro.html', data)