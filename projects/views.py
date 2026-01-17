from rest_framework import viewsets
from .models import Project, Prompt
from .serializers import ProjectSerializer, PromptSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PromptViewSet(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prompt.objects.filter(project_id=self.kwargs['project_id'])
    
    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs['project_id'])
