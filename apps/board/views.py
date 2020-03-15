from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, serializers

from .models import Board
from .serializers import BoardSerializer
from .permissions import IsAuthorOrReadOnly

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # author = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]