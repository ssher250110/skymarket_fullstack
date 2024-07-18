from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ads.filters import MyAdTitleFilter
from ads.models import Ad, Comment
from ads.permissions import IsAuthor
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


class AdListCreateAPIView(ListCreateAPIView):
    """ Создание объявления и просмотр списка объявлений """

    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["title", "price"]
    filterset_class = MyAdTitleFilter

    def get_serializer_class(self):
        """ Получение сериализатора по условиям """

        if self.request.method == "POST":
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        """ Добавление автора объявления """

        serializer.save(author=self.request.user)


class AdRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Просмотр, изменение и удаление одного объявления """

    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer

    def get_permissions(self):
        """ Получение прав доступа по условиях """

        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser | IsAuthor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class AdUserListAPIView(ListAPIView):
    """ Просмотр пользовательского списка объявлений  """

    serializer_class = AdSerializer
    permission_classes = [IsAdminUser | IsAuthor]
    filter_backends = [OrderingFilter]
    ordering_fields = ["title", "price"]

    def get_queryset(self):
        """ Получение набора данных по условию """

        return Ad.objects.filter(author=self.request.user)


class CommentListCreateAPIView(ListCreateAPIView):
    """ Создание отзыва и просмотр списка отзывов"""
    serializer_class = CommentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["title", "created_at"]

    def get_queryset(self):
        """ Получение набора данных по условию """

        ad = self.kwargs.get("ad")
        return Comment.objects.filter(ad=ad)

    def perform_create(self, serializer):
        """ Добавление автора отзыва """

        serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ Просмотр, изменение и удаление одного отзыва """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """ Получение набора данных по условиям """

        ad = self.kwargs.get("ad")
        pk = self.kwargs.get("pk")
        return Comment.objects.filter(ad=ad, pk=pk)

    def get_permissions(self):
        """ Получение прав доступа по условиях """

        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser | IsAuthor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
