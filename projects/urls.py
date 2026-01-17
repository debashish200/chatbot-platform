from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProjectViewSet, PromptViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

prompt_list = PromptViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_id>/prompts/', prompt_list, name='project-prompts'),
]
