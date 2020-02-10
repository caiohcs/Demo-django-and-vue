from django.shortcuts import render
from .models import Technology
from .serializers import TechnologySerializer
from rest_framework import generics


class TechnologyList(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TechnologyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
