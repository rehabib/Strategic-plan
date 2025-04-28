from django.db import models
from django.contrib.auth import get_user_model
from backend.models.perspective import Perspective
from backend.models.astrategic_goal import AstrategicGoal
from backend.models.measurement import Measurement
from backend.models.user_profile import UserProfile


User = get_user_model()

class AgencyPlan(models.Model):
    class Meta:
        app_label  = "core"
    
   
    agency=models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True,related_name='agency_plans')   
    perspective = models.ForeignKey(Perspective, on_delete=models.SET_NULL, null=True, blank=True)
    astrategic_goal = models.ForeignKey(AstrategicGoal, on_delete=models.SET_NULL, null=True, blank=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True, blank=True)
    base_value = models.FloatField(blank=True, null=True)
    aim = models.FloatField(blank=True, null=True)
    year  = models.IntegerField(blank=True, null=True)
    main_activity = models.TextField(blank=True, null=True)
    beneficial_society = models.TextField(blank=True, null=True)
    beneficial_body = models.TextField(blank=True, null=True)
    budget_government = models. FloatField(blank=True, null=True)
    budget_society = models.FloatField(blank=True, null=True)
    other_budget = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


   
    def __str__(self): 
        return f"{self.perspective}-{self.astrategic_goal} - {self.measurement} - {self.year}"
    
    
