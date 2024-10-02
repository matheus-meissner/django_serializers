from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Define o conjunto de dados para o ViewSet
    serializer_class = PostSerializer  # Associa o serializer ao ViewSet
