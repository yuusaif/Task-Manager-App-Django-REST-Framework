from django.urls import path
from .views import RegisterView, MyTokenObtainPairView, ProfileReadUpdateView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileReadUpdateView.as_view(), name='profile'),
    path('profile/update', ProfileReadUpdateView.as_view(), name='profile-update'),
    path('token/', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
