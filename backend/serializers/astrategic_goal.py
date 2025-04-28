# core/serializers/astrategic_goal_serializer.py

from rest_framework import serializers
from backend.models.astrategic_goal import AstrategicGoal


class AstrategicGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstrategicGoal
        fields = "__all__"
