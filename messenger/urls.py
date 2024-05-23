from django.urls import path
from messenger import views

urlpatterns = [
    path('users/', views.chat_users),
]