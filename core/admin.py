from django.contrib import admin

# Register your models here.
from backend.models.agency_plan import AgencyPlan
from backend.models.director_plan import DirectorPlan
from backend.models.department import Department
from backend.models.perspective import Perspective
from backend.models.astrategic_goal import AstrategicGoal
from backend.models.dstrategic_goal import DstrategicGoal
from backend.models.measurement import Measurement
from backend.models.activity import Activity
from backend.models.user_profile import UserProfile

admin.site.register(AgencyPlan)
admin.site.register(DirectorPlan)
admin.site.register(Perspective)
admin.site.register(AstrategicGoal)
admin.site.register(DstrategicGoal)
admin.site.register(Measurement)
admin.site.register(Activity)
admin.site.register(Department)
admin.site.register(UserProfile)