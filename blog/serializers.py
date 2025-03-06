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
    duration = serializers.IntegerField(source='duration.value')
    links = LinkSerializer(many=True)

    class Meta:
        model = models.Post
        fields = "__all__"


class PostSerializerSummary(serializers.ModelSerializer):
    post_type = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'post_type']
        
    def get_post_type(self, obj):
        
        post_type = ""
        if obj.video:
            post_type = "video"
        elif obj.audio:
            post_type = "audio"
        elif obj.links:
            post_type = "social"
            
        return post_type