from rest_framework import serializers
from .models import MyChannel

class MyChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyChannel
        fields = ['id', 'user', 'name', 'description', 'subscriberCount', 'videoCount']