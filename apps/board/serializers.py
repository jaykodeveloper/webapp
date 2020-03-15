from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('id', 'author', 'title', 'body', 'image', 'created','updated')
