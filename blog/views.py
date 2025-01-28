from rest_framework import permissions, viewsets

from blog import serializers
from blog import models


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """ Filter in get params """
        
        queryset = models.Post.objects.all()
        
        # Filter by group
        group = self.request.query_params.get("group", None)
        if group:
            queryset = queryset.filter(group__id=group)
            
        # Filter by category
        category = self.request.query_params.get("category", None)
        if category:
            queryset = queryset.filter(category__id=category)
            
        # Filter by duration
        duration = self.request.query_params.get("duration", None)
        if duration:
            queryset = queryset.filter(duration__value=duration)
            
        return queryset


class RandomPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """ Filter in get params """
        
        queryset = models.Post.objects.all()
        
        # Get random post
        queryset = queryset.order_by("?")[:1]
        
        return queryset