# este archivo serializa el modelo de forma que
# pueda ser transportado al protocolo http
from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    # definimos con que clase y campos trabajar en meta
    class Meta:
        model = Country
        fields = '__all__'
