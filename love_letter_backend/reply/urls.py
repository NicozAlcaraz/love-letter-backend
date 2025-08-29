from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reply.views import ReplyViewset

app_name = "reply"

router = DefaultRouter()
router.register(r"", ReplyViewset, basename="reply")

urlpatterns = [path("", include(router.urls))]