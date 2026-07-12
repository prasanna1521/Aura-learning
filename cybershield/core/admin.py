from django.contrib import admin
from .models import LearnerProfile

@admin.register(LearnerProfile)
class LearnerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_language', 'assigned_level', 'literacy_score', 'daily_target_minutes')
    list_filter = ('assigned_level', 'preferred_language')
    search_fields = ('user__username', 'user__email')
