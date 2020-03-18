from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from ..board.models import Board

# class UserSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # boards = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Board.objects.all()
    # )
    boards = serializers.HyperlinkedRelatedField(
        view_name='board:board-detail',
        lookup_field='pk',
        many=True, 
        queryset=Board.objects.all()
    )
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        lookup_field='pk',
        view_name="users:user-detail")


    class Meta:
        model = User
        # fields = ('id', 'username', 'boards')
        fields = ('url', 'id', 'username', 'boards')

class CreateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        lookup_field='pk',
        view_name="users:user-detail")

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], None, validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password')

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("unable to log in with provided credential")