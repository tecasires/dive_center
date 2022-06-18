# Necesitaremos importar el objeto 'HttpResponse' para poder trabajar con él.
from django.http import HttpResponse

# Importamos el render que vamos a utilizar.
from django.shortcuts import render


# Definimos nuestra primera vista llamada 'my_view' en la que le decimos que al realizarnos un request devuelva el mensaje 'Esta es mi vista'.
def my_view(request):
    return HttpResponse('Esta es mi vista')

# Definimos nuestra vista 'my_template' para ser cargada con el render.
def my_template(request):
	return render(request, "my_template.html", context = {})

# Definimos nuestra vista 'index' para ser cargada con el render.
def index(request):
    return render(request, "index.html", context = {})
