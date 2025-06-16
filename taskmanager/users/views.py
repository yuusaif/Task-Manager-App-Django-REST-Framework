from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import ProfileSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import generics, permissions
from .models import Profile
from rest_framework.permissions import IsAuthenticated, AllowAny

# Register new profile + user
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

# JWT login with user info
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Read or Update Profile
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get_or_create(user=self.request.user)[0]
    
