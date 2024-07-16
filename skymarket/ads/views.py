from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ads.filters import MyAdTitleFilter
from ads.models import Ad, Comment
from ads.permissions import IsAuthor
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


class AdListCreateAPIView(ListCreateAPIView):
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["title", "price"]
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

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser | IsAuthor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class AdUserListAPIView(ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAdminUser | IsAuthor]
    filter_backends = [OrderingFilter]
    ordering_fields = ["title", "price"]

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["title", "created_at"]

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

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser | IsAuthor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
