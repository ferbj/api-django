from django.contrib import admin

# Register your models here.
from .models import User, Curso, Coordinador

Models = [User,Coordinador,Curso]
admin.site.register(Models)



