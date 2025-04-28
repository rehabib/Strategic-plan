from django.db import models
from backend.models.department import Department
from django.contrib.auth import get_user_model
from backend.models.perspective import Perspective
from backend.models.measurement import Measurement
from backend.models.activity import Activity
from backend.models.user_profile import UserProfile

User = get_user_model()

class DirectorPlan(models.Model):
    
    class Meta:
        app_label  = "core"

    number = models.IntegerField(blank=True, null=True) 
    director = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True,related_name='director_plans')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    perspective = models.ForeignKey(Perspective,on_delete=models.SET_NULL,blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL,blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    dstrategic_goal = models.CharField(max_length=255, blank=True, null=True)
    measurement = models.ForeignKey(Measurement,on_delete=models.SET_NULL, blank=True, null=True)
    budget_year_aim = models.FloatField(blank=True, null=True)
    july = models.FloatField(blank=True, null=True)
    august = models.FloatField(blank=True, null=True)
    september  = models.FloatField(blank=True, null=True)
    october = models.FloatField(blank=True, null=True)
    november = models.FloatField(blank=True, null=True)
    december = models.FloatField(blank=True, null=True)
    january = models. FloatField(blank=True, null=True)
    february = models.FloatField(blank=True, null=True)
    march = models.FloatField(blank=True, null=True)
    april = models.FloatField(blank=True, null=True)
    may = models.FloatField(blank=True, null=True)
    june = models.FloatField(blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    expected_result = models.CharField(max_length=255, blank=True, null=True)
    acountable_person = models.CharField(max_length=255, blank=True, null=True)
    
   
    class Meta:
        app_label  = "core"
    
    def __str__(self): 
        return f"{self.department.name if self.department else 'No Department'}-{self.perspective} - {self.dstrategic_goal} - {self.measurement}"