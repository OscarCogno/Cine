from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Director, Film

def index(request):
    num_film = Film.objects.all().count()
    num_director = Director.objects.all().count()
    num_genero = Genre.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_film': num_film,
            'num_director': num_director,
            'num_genero': num_genero
        }
    )

