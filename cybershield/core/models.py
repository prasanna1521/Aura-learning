from django.db import models
from django.contrib.auth.models import User

class LearnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    preferred_language = models.CharField(max_length=50, default='English')
    age = models.IntegerField(null=True, blank=True)
    literacy_score = models.IntegerField(default=0)
    assigned_level = models.CharField(max_length=50, default='Beginner')
    daily_target_minutes = models.IntegerField(default=15)

    def __str__(self):
        return f"{self.user.username} - {self.assigned_level}"
