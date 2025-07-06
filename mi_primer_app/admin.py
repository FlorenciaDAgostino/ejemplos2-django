from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso 

register_models = [Familiar, Curso]

admin.site.register(register_models)