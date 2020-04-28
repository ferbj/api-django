
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name='main/index.html'

def cursos(response):
  cursos = Curso.objects.all()
  return render(response,"cursos/cursos.html",{"cursos":cursos})