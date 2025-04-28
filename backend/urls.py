from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers



# Backend Views
from backend.views.agency_views import AgencyPlanViewSet
from backend.views.director_views import DirectorPlanViewSet
from backend.views.perspective import PerspectiveViewSet
from backend.views.astrategic_goal import AstrategicGoalViewSet
from backend.views.dstrategic_goal import DstrategicGoalViewSet
from backend.views.measurement import MeasurementViewSet
from backend.views.activity import ActivityViewSet
from backend.views.department import DepartmentViewSet
from backend.views.user_profile import UserProfileViewSet

# Routers
router = routers.DefaultRouter()

router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'agency-plan', AgencyPlanViewSet, basename='agencyplan')
router.register(r'director-plan', DirectorPlanViewSet, basename='directorplan')
router.register(r'perspective', PerspectiveViewSet, basename='perspective')
router.register(r'astrategic-goal', AstrategicGoalViewSet, basename='astrategicgoal')
router.register(r'dstrategic-goal', DstrategicGoalViewSet, basename='dstrategicgoal')
router.register(r'measurement', MeasurementViewSet, basename='measurement')
router.register(r'activity', ActivityViewSet, basename='activity')
router.register(r'user-profile', UserProfileViewSet, basename='userprofile')



# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Optional: you could namespace it too if needed
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
