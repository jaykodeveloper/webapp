from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User

class BoardSerializer(serializers.ModelSerializer):
    # this needs to have read_only attribute
    author = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Board
        fields = ('id', 'author', 'title', 'body', 'image', 'created','updated')
