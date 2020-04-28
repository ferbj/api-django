from nt import truncate
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import User, Curso, Coordinador
from .serializer import UserSerializer,CursoSerializer,CoordinadorSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class CoordinadorViewSet(viewsets.ModelViewSet):
  queryset = Coordinador.objects.all()
  serializer_class = CoordinadorSerializer 