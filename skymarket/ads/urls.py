from django.urls import path

from ads.apps import SalesConfig
from ads.views import AdCreateAPIView, CommentCreateAPIView, AdUpdateAPIView, CommentUpdateAPIView

app_name = SalesConfig.name

urlpatterns = [
    path("api/ads/", AdCreateAPIView.as_view(), name="ad-create"),
    path("api/ads/<int:pk>/", AdUpdateAPIView.as_view(), name="ad-update"),

    path("api/ads/<int:pk>/comments/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("api/ads/<int:ad_pk>/comments/<int:pk>/", CommentUpdateAPIView.as_view(), name="comment-update")
]
