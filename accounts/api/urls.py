from django.urls import path, include
# from api.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)
from . import views



urlpatterns = [
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/registration/',views.RegstrationUser.as_view(),name='registration'),
    path('api/users',views.RetriveUsers.as_view(),name='users'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]