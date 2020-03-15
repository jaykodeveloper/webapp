from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('id', 'author', 'title', 'body', 'image', 'created','updated')

# class UserSerializer(serializers.ModelSerializer):
#     board_field = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Board.objects.all()
#     )

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'board_field')