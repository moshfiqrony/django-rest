from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=False, null=False)
    logo_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.domain


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    icon_link = models.CharField(max_length=1000, blank=True, null=True)
    bg_color = models.CharField(max_length=10, blank=True, null=True)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    meta = models.CharField(max_length=255, blank=True, null=True)
    assets = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    question_type_id = models.ForeignKey(QuestionType, models.CASCADE)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.question_id)


class FeedbackSharing(models.Model):
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_id = models.ForeignKey(Feedback, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shared_with)
