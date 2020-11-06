from django.db import models

# Create your models here.
op_contacto = [
    [0, "Producto"],
    [1, "Pedido"],
    [2, "Felicitaciones"],
    [3, "Reclamos"]

]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    tfono = models.IntegerField
    motivo = models.IntegerField(choices=op_contacto)
    email = models.EmailField
    mensaje = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre