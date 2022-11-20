from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('application', views.ApplicationViewSet, basename='application')
router.register('users', views.UserViewSet )

urlpatterns = [
    path('api/', include(router.urls)),
    
]
