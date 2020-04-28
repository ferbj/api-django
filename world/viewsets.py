from django.http import HttpResponse
from rest_framework import viewsets

from nt import truncate

from .models import Country
from .serializer import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


def truncate(request):
    if request.method=='POST':
        return HttpResponse(Country.objects.all().delete())
