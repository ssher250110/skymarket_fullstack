from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "phone", "image"]


class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name", "id"]
