from rest_framework import serializers
from .models import Todo


class Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'completed',
            'date'
        )
        model = Todo
        