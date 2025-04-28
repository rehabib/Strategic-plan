from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.models.department import Department

class UserProfile(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('agency', 'Agency'),
        ('director', 'Director'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
  

    # Adding related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='userprofile_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='userprofile_set', 
        blank=True
    )
    class Meta:
        app_label = "core"
        
        def __str__(self):
           return f"{self.role} - {self.get_role_display()}"
