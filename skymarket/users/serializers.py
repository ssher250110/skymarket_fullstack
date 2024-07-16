from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """ Сериализатор для регистрации пользователя """
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "phone", "image"]


class CurrentUserSerializer(ModelSerializer):
    """ Сериализатор текущего пользователя """
    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name", "pk"]
