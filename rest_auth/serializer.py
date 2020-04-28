from rest_framework import serializers
from .models import User, Curso, Coordinador

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = '__all__'

class CoordinadorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coordinador
    fields = '__all__'  