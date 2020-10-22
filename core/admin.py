from django.contrib import admin
from core.models import *



"""---------------------------------------------------------------------------------"""


class MatDeLecSup(admin.ModelAdmin):
    list_display = ['creador', 'nombre', 'fecha_publicacion', 'material']

class LibroSup(admin.ModelAdmin):
    list_display = ['Biblioteca','creador','nombre','editorial','fecha_publicacion','estado','foto']

class RevistaSup(admin.ModelAdmin):
    list_display = ['Biblioteca','creador','nombre','titular','fecha_publicacion','estado', 'foto']


"""---------------------------------------------------------------------------------"""


class PersonaSup (admin.ModelAdmin):
    list_display = ['nombre','apellido','mail','cell']

class AlumnoSup(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cell', 'mail', 'matricula', 'cantLibros']

class ProfesorSup(admin.ModelAdmin):
    list_display = ['nombre','apellido','mail','cell','numEmpleado']


"""---------------------------------------------------------------------------------"""





"""---------------------------------------------------------------------------------"""


admin.site.register(DT)
admin.site.register(Jugador)
admin.site.register(Mercado)
admin.site.register(VendJug)
admin.site.register(CompJug)
admin.site.register(Usuario)

