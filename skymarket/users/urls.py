from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

app_name = UsersConfig.name

urlpatterns = [
    path("", include(users_router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
