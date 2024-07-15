from rest_framework.routers import SimpleRouter

from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet

app_name = SalesConfig.name

router = SimpleRouter(trailing_slash=False)
router.register("api/ads/", AdViewSet)
router.register("api/ads/<int:pk>/comments/", CommentViewSet)

urlpatterns = router.urls
