from django.urls import path
from .views import PromptViewSet

prompt_list = PromptViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('<int:project_id>/prompts/', prompt_list, name='project-prompts'),
]
