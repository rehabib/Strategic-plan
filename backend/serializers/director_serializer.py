# serializers/director_plan_serializer.py
from rest_framework import serializers
from backend.models.director_plan import DirectorPlan

class DirectorPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorPlan
        fields = [
            'id', 'director', 'department', 'perspective', 'activity',
            'weight', 'dstrategic_goal', 'measurement', 'budget_year_aim',
            'july', 'auguest', 'september', 'october', 'november', 'december',
            'january', 'february', 'march', 'april', 'may', 'june',
            'budget', 'expected_result', 'acountable_person',
            'plan_name', 'plan_description'
        ]
