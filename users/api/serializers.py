from rest_framework import serializers
from ..models import UserProfile


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user_id', 'email', 'is_active', 'is_admin', 'is_manager', 'is_org_admin', 'is_stuff')

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)
