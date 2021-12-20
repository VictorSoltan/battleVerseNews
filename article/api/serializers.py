from rest_framework import serializers

from ..models import Article

# _______OVERVIEW_________ 

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
  
