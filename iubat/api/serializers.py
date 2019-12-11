from rest_framework import serializers
from iubat.models import StudentProfile

class StudentProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('id', 'user_id', 'firstname', 'lastname', 'personal_email')

    def create(self, validated_data):
        return StudentProfile.objects.create(**validated_data)
