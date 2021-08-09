from django.shortcuts import render , redirect
from .models import Users #se debe importar el modelo para trabajarlo en la vista (controlador , es como el servlet)

def index(request):
    
    if request.method == 'GET':
        contexto = {
            'usuarios' : Users.objects.all() #esto es igual que un SELECT usuarios FROM User; 
        }
        return render(request, 'users_app/index.html' , contexto)

def procesar(request):

    if request.method == 'POST':
        print(request.POST)

        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        edad = request.POST['edad']
        # estos son todos los datos del fomulario y lo que esta '' es el nombre que tiene en el name="delHtml"

        usuario = Users.objects.create(
            nombre = nombre, 
            apellido = apellido,
            email = email,
            edad = edad
            )

        return redirect('/')
        # el redirect reenvia siempre en methodo GET

