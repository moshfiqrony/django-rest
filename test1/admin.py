from django.contrib import admin
from .models import Feedback, Question, QuestionType, Skill, Organization, FeedbackSharing

# Register your models here.
admin.site.register(Feedback)
admin.site.register(FeedbackSharing)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Skill)
admin.site.register(Organization)
