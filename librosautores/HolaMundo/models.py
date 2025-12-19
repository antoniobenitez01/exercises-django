from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField (
        verbose_name= 'Nombre',
        max_length= 100,
        default= ''
    )
    last_name=models.CharField(
        verbose_name="Apellido",
        max_length= 150,
        default= ""
    )
    age = models.PositiveSmallIntegerField (verbose_name="Edad")
    
    def __str__(self):
        return f'{self.name} {self.last_name}'

class Book (models.Model):
    title = models.CharField(
        "Título del Libro",
        max_length=225,
        unique=True
    )
    cod = models.CharField(
        "Código",
        max_length= 15,
        unique= True
    )
    author = models.ManyToManyField(Author)
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
    
    def __str__(self):
            return self.title