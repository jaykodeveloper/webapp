from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from rest_framework import generics, serializers

from .models import Board
from .serializers import BoardSerializer

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    # author = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


"""
class BoardList(ListView):
    model = Board
    template_name_suffix = '_list'

class BoardCreate(CreateView):
    model = Board
    field = ['title', 'body', 'created', 'image']
    template_name_suffix = '_create'
    success_url = '/'

class BoardUpdate(UpdateView):
    model = Board
    field = ['title', 'body', 'created', 'image']
    template_name_suffix = '_update'
    success_url = '/'

class BoardDelete(DeleteView):
    model = Board
    template_name_suffix = '_delete'
    success_url = '/'

class BoardDetail(DetailView):
    model = Board
    template_name_suffix = '_detail'
"""
