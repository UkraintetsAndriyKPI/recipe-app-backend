from django.shortcuts import render
from rest_framework import viewsets

from .models import Categories, Tag
from .serializers import CategoriesSerializer, TagSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
