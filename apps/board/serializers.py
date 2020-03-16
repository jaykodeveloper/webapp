from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User

# class BoardSerializer(serializers.ModelSerializer):
class BoardSerializer(serializers.HyperlinkedModelSerializer):
    # this needs to have read_only attribute
    # author = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )
    # author = serializers.HyperlinkedRelatedField(
    #     view_name='users-detail', 
    #     lookup_field='username',
    #     read_only=True, 
    #     default=serializers.CurrentUserDefault()
    # )
    author = serializers.ReadOnlyField(source='author.username')
    url = serializers.HyperlinkedIdentityField(
        view_name="board-detail",
        read_only=True,
        lookup_field='id')
    class Meta:
        model = Board
        # fields = ('id', 'author', 'title', 'body', 'image', 'created','updated')
        fields = ('url','id', 'author', 'title', 'body', 'image', 'created','updated')
        view_name='board-detail'
        lookup_field='id'
