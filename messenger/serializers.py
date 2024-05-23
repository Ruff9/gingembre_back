from rest_framework import routers,serializers,viewsets
from .models import ChatUser


class ChatUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatUser
        fields = ['id', 'username', 'created_at']