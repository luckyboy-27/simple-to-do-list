from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Todo
from .serializers import Serializer

class TodoViewSet(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Serializer