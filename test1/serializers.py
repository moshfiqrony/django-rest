from rest_framework import serializers

from .models import Organization, Skill, Question, FeedbackSharing, Feedback


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'domain', 'logo_link')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'icon_link', 'bg_color', 'organization_id')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'updated_on', 'created_on', 'organization_id', 'skill_id', 'question_type_id')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'question_id', 'created_by')


class FeedbackSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackSharing
        fields = ('id', 'shared_with', 'feedback_id')
