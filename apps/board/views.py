from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Board
from .serializers import BoardSerializer
from .permissions import IsAuthorOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'boards': reverse('board:board-list', request=request, format=format)
    })


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # author = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )
    author = serializers.HyperlinkedRelatedField(
        view_name='users-detail', 
        lookup_field='username',
        read_only=True, 
        default=serializers.CurrentUserDefault()
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]