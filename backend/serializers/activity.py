# core/serializers/astrategic_goal_serializer.py

from rest_framework import serializers
from backend.models.activity import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
