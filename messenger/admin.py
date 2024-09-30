from django.contrib import admin
from .models import ChatUser


class ChatUserAdmin(admin.ModelAdmin):
    model = ChatUser
    fields = ["username", "created_at"]
    list_display = ["username", "created_at"]

admin.site.register(ChatUser)
