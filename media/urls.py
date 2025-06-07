from django.urls import path
from rest_framework import routers

from media.views import PhotoBackupView, TestView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('backup', PhotoBackupView.as_view()),
    path('test-post', TestView.as_view())
]