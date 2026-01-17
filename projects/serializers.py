from rest_framework import serializers
from .models import Project, Prompt


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']

class PromptSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source='project.id')

    class Meta:
        model = Prompt
        fields = ['id', 'project', 'content']
