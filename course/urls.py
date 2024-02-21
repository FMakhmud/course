from core import urls
from django.urls import path
from .views import LessonsAPIView

urlpatterns = [
    path('lessons-list/', LessonsAPIView.as_view())
]
