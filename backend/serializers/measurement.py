# core/serializers/astrategic_goal_serializer.py

from rest_framework import serializers
from backend.models.measurement import Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"
