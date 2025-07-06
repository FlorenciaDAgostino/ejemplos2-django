from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante, Profesores 

register_models = [Familiar, Curso, Estudiante, Profesores]

admin.site.register(register_models)