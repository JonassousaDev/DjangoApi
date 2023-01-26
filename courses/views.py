from django.shortcuts import render
from rest_framework import viewsets
from .models import Curse
from .serializers import CurseSerializer

class CurseViewSet(viewsets.ModelViewSet):
    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
