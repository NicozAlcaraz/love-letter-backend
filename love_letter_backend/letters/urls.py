from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reply.views import LettersViewset

app_name = "letters"

router = DefaultRouter()
router.register(r"", LettersViewset, basename="letters")

urlpatterns = [path("", include(router.urls))]