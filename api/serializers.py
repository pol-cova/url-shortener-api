from rest_framework import serializers
from .models import Url

# Url serializer
class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['url']