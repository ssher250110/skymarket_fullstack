from django.urls import path

from ads.apps import SalesConfig
from ads.views import AdListCreateAPIView, AdRetrieveUpdateDestroyAPIView, AdListAPIView, CommentListCreateAPIView

app_name = SalesConfig.name

urlpatterns = [
    path("api/ads/", AdListCreateAPIView.as_view(), name="ad-list-create"),
    path("api/ads/<int:pk>/", AdRetrieveUpdateDestroyAPIView.as_view(), name="ad-retrieve-update-destroy"),
    path("api/ads/me/", AdListAPIView.as_view(), name="ad-list-me"),

    path("api/ads/<int:ad>/comments/", CommentListCreateAPIView.as_view(), name="comment-list-create")
]
