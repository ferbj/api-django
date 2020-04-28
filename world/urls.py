from rest_framework import routers
from .viewsets import CountryViewSet

router = routers.SimpleRouter()
router.register('countries', CountryViewSet)
urlpatterns = router.urls