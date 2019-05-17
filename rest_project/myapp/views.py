from django.shortcuts import render

# Create your views here.
from .models import Ticks
from rest_framework import viewsets
from myapp.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ticks.objects.all()
    serializer_class = UserSerializer

