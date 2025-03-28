from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverRegisterViewSet
from driverapp.views import DriverComplaintListView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from driverapp.views import *
# Create API documentation schema
schema_view = get_schema_view(
    openapi.Info(
        title="Location Based Garbage Collecting App",
        default_version='v1',
        description="API for driver registration and management",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Create router and register Driver API
router = DefaultRouter()
router.register(r'drivers', DriverRegisterViewSet, basename='drivers')

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include driver registration routes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('login/', DriverLoginView.as_view(), name='driver_login'),
    path('driver-complaints/<int:driver_id>/', DriverComplaintListView.as_view(), name='driver-complaints'),
     path('complaint-status/<int:complaint_id>/', UpdateComplaintStatusView.as_view(), name='update-complaint-status'),
     
]
