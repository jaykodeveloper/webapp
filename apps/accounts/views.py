from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import UserSerializer

@api_view(['GET'])
def api_root(req, format=None):
    return Response({
        'users': reverse('users:user-list', request=req, format=format),
    })
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer