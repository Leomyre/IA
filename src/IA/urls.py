from django.urls import path
from . import views

urlpatterns = [
    path('call-ai/', views.call_ai_api, name='call_ai'),
     path("", views.ai_prompt, name="ai_prompt"),
]
