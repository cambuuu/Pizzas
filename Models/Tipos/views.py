'''from django.http import HttpRequest
from django.shortcuts import render

from Models.Tipos.forms import armar


class armarView(HttpRequest):
    def index(request):
        armarpizza = armar()
        return render(request,"ArmarIndex.html", {"form":armarpizza})
    def procesar_formulario(request):
        armarpizza = armar(request.POST)
        if armarpizza.is_valid():
            armarpizza.save()
            armarpizza = armar()
        return render(request,"ArmarIndex.html", {"form":armarpizza,"mensaje: ": 'Agregado correctamente'})
'''