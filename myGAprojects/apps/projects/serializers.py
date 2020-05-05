from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'category','description', 'url', 'image', 'created_at', 'updated_at')
        # lookup_field = 'category'
