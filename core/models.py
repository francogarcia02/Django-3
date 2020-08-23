from django.db import models

Estado_Libro = [
    ('IN','En la biblioteca'),
    ('BW','Prestado'),
    ('RQ','Pedido'),
    ('RV','Reservado'),
]

class Biblioteca(models.Model):
    pass
"""---------------------------------------------------------------------------------"""


class Prestamo(models.Model):
    id = models.IntegerField(primary_key = True)
    codigo = models.CharField(max_length=50)
    fcha_salida = models.CharField(max_length = 40, default='reescribir')
    fcha_regreso = models.CharField(max_length = 40, default='reescribir')

    def __str__(self):
        return self.codigo


"""---------------------------------------------------------------------------------"""


class Persona(models.Model):
    Biblioteca = models.ForeignKey(Biblioteca, null=True, blank=True, on_delete=models.CASCADE)
    Prestamo = models.OneToOneField(Prestamo, null=True, blank=True, on_delete=models.CASCADE)
    tipoPersona = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    cell = models.IntegerField()
    cantLibros = models.IntegerField()
    adeudo = models.FloatField()

    def __str__(self):
        return self.nombre

class Alumno(Persona):
    matricula = models.IntegerField()

    def __str__(self):
        return self.nombre

class Profesor(Persona):
    numEmpleado = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Profesores'


"""---------------------------------------------------------------------------------"""


class MatDeLec(models.Model):
    Biblioteca = models.ForeignKey(Biblioteca, null=True, blank=True, on_delete=models.CASCADE)
    Prestamo = models.ForeignKey(Prestamo, null=True, blank=True, on_delete=models.CASCADE)
    material = models.CharField(max_length=60, default='reescribir')
    codigo = models.CharField(max_length=60)
    nombre= models.CharField(max_length=50)
    fecha_publicacion = models.CharField(max_length = 40)
    estado = models.CharField(choices=Estado_Libro, default='En la biblioteca',max_length=2)
    creador = models.CharField(max_length=50, default='reescribir')


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = ('Material')
        verbose_name_plural = ('Materiales')


class Libro(MatDeLec):
    editorial = models.CharField(max_length = 50)
    foto = models.ImageField(default='fotos_tap/default.png', blank=True, max_length=100, upload_to='fotos_tap/')

    def __str__(self):
        return self.editorial


class Revista(MatDeLec):
    foto = models.ImageField(default='fotos_tap/default.png', blank=True, max_length=100, upload_to='fotos_tap/')
    titular = models.CharField(max_length=50)

    def __str__(self):
        return self.titular

"""---------------------------------------------------------------------------------"""