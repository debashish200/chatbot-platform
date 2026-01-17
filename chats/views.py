import requests
import os
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from projects.models import Project, Prompt
from .models import Chat

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        project_id = request.data.get("project_id")
        message = request.data.get("message")

        project = Project.objects.get(id=project_id)
        prompt = Prompt.objects.filter(project=project).last()

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {"role": "system", "content": prompt.content if prompt else ""},
                {"role": "user", "content": message}
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

        ai_reply = response.json()["choices"][0]["message"]["content"]

        Chat.objects.create(
            user=request.user,
            project=project,
            user_message=message,
            ai_response=ai_reply
        )

        return Response({"reply": ai_reply})
