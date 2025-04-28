# serializers/agency_plan_serializer.py
from rest_framework import serializers
from backend.models.agency_plan import AgencyPlan

class AgencyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyPlan
        fields = [
            'id', 'agency', 'perspective', 'strategic_goal', 'measurement',
            'base_value', 'aim', 'year', 'main_activity', 
            'beneficial_society', 'beneficial_body', 
            'budget_government', 'budget_society', 'other_budget',
            'created_at', 'plan_name', 'plan_description'
        ]
        read_only_fields = ['created_at']
