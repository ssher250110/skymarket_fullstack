from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, get_object_or_404

from ads.filters import MyAdTitleFilter
from ads.models import Ad, Comment
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


class AdListCreateAPIView(ListCreateAPIView):
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MyAdTitleFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdUserListAPIView(ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad = self.kwargs.get("ad")
        return Comment.objects.filter(ad=ad)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        print()
        ad = self.kwargs.get("ad")
        pk = self.kwargs.get("pk")
        return Comment.objects.filter(ad=ad, pk=pk)
