# core/views/astrategic_goal_view.py

from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response
from backend.models.activity import Activity  # Corrected the import statement 
from backend.serializers.activity import ActivitySerializer
from backend.serializers.measurement import MeasurementSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()  # Corrected the model to AstrategicGoal
    serializer_class = ActivitySerializer  # Corrected the serializer class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
