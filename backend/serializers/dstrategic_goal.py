# core/serializers/astrategic_goal_serializer.py

from rest_framework import serializers
from backend.models.dstrategic_goal import DstrategicGoal

class DstrategicGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DstrategicGoal
        fields = "__all__"
