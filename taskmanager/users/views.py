from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ProfileSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import generics, status
from .models import Profile
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# Register new profile + user
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

# JWT login with user info
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

# Read or Update Profile
class ProfileReadUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get_or_create(user=self.request.user)[0]
    
# Logout by black listing refresh token
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Log out successful", status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response("Log out failed", status= status.HTTP_400_BAD_REQUEST)
    
