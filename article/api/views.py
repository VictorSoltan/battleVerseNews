from rest_framework import viewsets

from .serializers import post_serializer

from ..models import Article


class post_view(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = post_serializer