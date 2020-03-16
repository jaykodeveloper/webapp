from rest_framework import serializers
from django.contrib.auth.models import User

from ..board.models import Board

# class UserSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # boards = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Board.objects.all()
    # )
    boards = serializers.HyperlinkedRelatedField(
        view_name='board-detail',
        lookup_field='user_id',
        many=True, 
        queryset=Board.objects.all()
    )
    # url = serializers.HyperlinkedIdentityField(
    #     read_only=True,
    #     lookup_field='id',
    #     view_name="users:user-detail")
    class Meta:
        model = User
        # fields = ('id', 'username', 'boards')
        fields = ('url', 'id', 'username', 'boards')