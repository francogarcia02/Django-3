from django.db import models



"""---------------------------------------------------------------------------------"""


class Mercado(models.Model):
    id = models.IntegerField(primary_key = True)
    Jugadores = models.CharField(max_length=50)
    Precio = models.IntegerField()
    CantidadJugadores = models.CharField(max_length = 40)

    def __str__(self):
        return self.Jugadores


"""---------------------------------------------------------------------------------"""


class Jugador(models.Model):
    Club = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    Pocicion = models.CharField(max_length=50)
    Edad = models.IntegerField()
    CantGoles = models.IntegerField(default=0)
    MediaPases= models.IntegerField(default=0)
    Mediatiros = models.IntegerField(default=0)
    MediaRegates = models.IntegerField(default=0)
    MediaDefenza = models.IntegerField(default=0)
    MediaFisico = models.IntegerField(default=0)
    MediaRitmo = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


"""---------------------------------------------------------------------------------"""


class DT(models.Model):
    Historia = models.CharField(max_length=60, default='reescribir')
    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Club = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


"""---------------------------------------------------------------------------------"""
class CompJug(models.Model):
    pass

class VendJug(models.Model):
    pass

"""---------------------------------------------------------------------------------"""

class Usuario(models.Model):
    id = models.IntegerField(primary_key = True)
    Nombre = models.CharField(max_length=50)
    Dinero = models.IntegerField()
    JugadoresPropios = models.CharField(max_length = 40)

    def __str__(self):
        return self.Nombre