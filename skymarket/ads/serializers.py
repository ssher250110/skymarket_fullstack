from rest_framework.fields import ReadOnlyField, ImageField
from rest_framework.serializers import ModelSerializer
from ads.models import Comment, Ad


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(ModelSerializer):
    phone = ReadOnlyField(source="author.phone")
    author_first_name = ReadOnlyField(source="author.first_name")
    author_last_name = ReadOnlyField(source="author.last_name")

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",
                  "author"]


class CommentSerializer(ModelSerializer):
    author_first_name = ReadOnlyField(source="author.first_name")
    author_last_name = ReadOnlyField(source="author.last_name")
    author_image = ImageField(source="author.image", read_only=True)

    class Meta:
        model = Comment
        fields = ["pk", "text", "author", "created_at", "author_first_name", "author_last_name", "ad",
                  "author_image"]
