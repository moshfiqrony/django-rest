from rest_framework import serializers
from iubat.models import StudentProfile

class StudentProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('id', 'user_id', 'firstname', 'lastname', 'personal_email')

    def create(self, validated_data):
        return StudentProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.save()
        return instance
