from django.contrib import admin

# Register your models here.
from .models import Genre, Director, Film

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Film)