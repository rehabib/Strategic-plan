from rest_framework import viewsets, status
from .permissions import IsAgency
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from backend.models.agency_plan import AgencyPlan
from backend.serializers.agency_serializer import AgencyPlanSerializer

class AgencyPlanViewSet(viewsets.ModelViewSet):
    queryset = AgencyPlan.objects.all()
    serializer_class = AgencyPlanSerializer
    permission_classes = [IsAuthenticated, IsAgency]

    def perform_create(self, serializer):
        serializer.save(agency=self.request.user)  # Automatically set agency user

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
