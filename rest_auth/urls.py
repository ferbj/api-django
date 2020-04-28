from rest_framework import routers
from .viewsets import UserViewSet, CursoViewSet,CoordinadorViewSet

from django.urls import include, path


router = routers.SimpleRouter()
router.register('users',UserViewSet)
router.register('cursos',CursoViewSet)
router.register('coordinarores',CoordinadorViewSet)

urlpatterns = router.urls