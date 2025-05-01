from django.urls import path
from rest_framework import routers

from media.views import FirstView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('hi', FirstView.as_view()),
]