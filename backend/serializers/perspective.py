# core/serializers/astrategic_goal_serializer.py

from rest_framework import serializers
from backend.models.perspective import Perspective

class PerspectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perspective
        fields = "__all__"
