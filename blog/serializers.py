from rest_framework import serializers

from blog import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = "__all__"


class DurationSerializer(serializers.Serializer):
    class Meta:
        model = models.Duration
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True)

    class Meta:
        model = models.Post
        fields = "__all__"
