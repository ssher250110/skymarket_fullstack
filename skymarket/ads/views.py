from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from ads.models import Ad, Comment
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


class AdListCreateAPIView(ListCreateAPIView):
    queryset = Ad.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdListAPIView(ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(ad=self.request.data["ad"])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
