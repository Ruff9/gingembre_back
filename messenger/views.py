from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import ChatUserSerializer
from .models import ChatUser


@csrf_exempt
def chat_users(request):
    if(request.method == 'GET'):
        chat_users = ChatUser.objects.all()
        serializer = ChatUserSerializer(chat_users, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = ChatUserSerializer(data=data)

        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)