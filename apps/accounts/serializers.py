from rest_framework import serializers
from django.contrib.auth.models import User

from ..board.models import Board

class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Board.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'boards')