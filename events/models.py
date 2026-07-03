from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    EVENT_CHOICES = [
        ('tech', 'Technical Symposium'),
        ('non-tech', 'Non-Technical Fest'),
        ('workshop', 'AI Workshop'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=150)
    email = models.EmailField()
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.event_type}"
