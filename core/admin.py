from django.contrib import admin
from core.models import *

class BibliotecaAdmin (admin.ModelAdmin):
    class EntryInLinesRevista(admin.TabularInline):
        model = Revista
    class EntryInLinesLibro(admin.TabularInline):
        model = Libro

    inlines = [EntryInLinesRevista]
    inlines = [EntryInLinesLibro]

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


class PrestamoSup(admin.ModelAdmin):
    list_display = ['id','codigo','fcha_salida','fcha_regreso',]


"""---------------------------------------------------------------------------------"""


admin.site.register(Biblioteca, BibliotecaAdmin)
admin.site.register(MatDeLec, MatDeLecSup)
admin.site.register(Libro, LibroSup)
admin.site.register(Revista, RevistaSup)
admin.site.register(Prestamo, PrestamoSup)
admin.site.register(Persona, PersonaSup)
admin.site.register(Alumno, AlumnoSup)
admin.site.register(Profesor, ProfesorSup)