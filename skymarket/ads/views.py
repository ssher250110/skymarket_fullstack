from rest_framework.generics import CreateAPIView, UpdateAPIView

from ads.models import Ad, Comment
from ads.serializers import AdDetailSerializer, CommentSerializer


class AdCreateAPIView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdUpdateAPIView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
