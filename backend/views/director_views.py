from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from backend.models.director_plan import DirectorPlan
from backend.serializers.director_serializer import DirectorPlanSerializer
from .permissions import IsDirector

class DirectorPlanViewSet(viewsets.ModelViewSet):
    queryset = DirectorPlan.objects.all()
    serializer_class = DirectorPlanSerializer
    permission_classes = [IsAuthenticated, IsDirector]

    def perform_create(self, serializer):
        serializer.save(director=self.request.user)  # Automatically set director user

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
