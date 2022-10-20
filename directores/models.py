from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse 

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Genero de la pelicula")

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=800, help_text="Descripcion de la pelicula")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)                 