from django.urls import path
from rest_framework import routers

from media.views import FirstView, TestView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('hi', FirstView.as_view()),
    path('test-post', TestView.as_view())
]