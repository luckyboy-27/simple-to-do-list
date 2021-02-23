from django.urls import path
from .views import TodoViewSet

urlpatterns = [
    path('', TodoViewSet.as_view()),
]
