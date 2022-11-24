from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('application', views.ApplicationViewSet, basename='application')
router.register('approved', views.ApplicationApproved, basename='approved')
router.register('appDelete', views.ApplicationDelete, basename="appDelete")
router.register('ApplicationSlot', views.ApplicationSlot, basename="ApplicationSlot")
router.register('crudApplication', views.ApplicationAllOperationViewset, basename="ApplicationAllOperationViewset")
router.register('application-modify', views.ApplicationModify, basename='application-modify'),

# router.register('users', views.UserViewSet )

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/StatusUpdate/<int:pk>/', views.StatusUpdate.as_view() , name='StatusUpdate'),
    path('api/getapplication/<int:pk>/', views.UserApplications.as_view(), name='getapplication'),
    path('api/slot-allocate/<int:application_id>/<int:slot_id>/', views.slotAllocate, name='slot-allocate'),
    path('api/waiting-list/', views.getWaitingApplication, name='getWaitingApplication'),
    path('api/booked-applicant/', views.getBookedApplicant, name='getBookedApplicant')
    
    
]
