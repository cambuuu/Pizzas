from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from Models.TipoPizza.forms import ContactoForm


class HomeView():

    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())
    def pagina1(self):
        return HttpResponse('hola nuevamente aweonanos')
    def pagina2(self, parametro1):
        return HttpResponse('hola aweonaos desde: ' + str(parametro1))
    def pagina3(self, parametro1, parametro2):
        return HttpResponse('Hola desde XD :' + str(parametro1) + ' - ' + str(parametro2))

    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())

    def quienes (self):
        plantilla = get_template('quienes.html')
        return HttpResponse(plantilla.render())
    def catalogo(self):
        plantilla = get_template('catalogo.html')
        return HttpResponse(plantilla.render())
    def contacto(request):
        data = {
            'form': ContactoForm()
        }
        if request.method == 'POST':
            formulario = ContactoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "Contacto guardado"
            else:
                data["form"] = formulario
        return render(request,'contacto.html', data)