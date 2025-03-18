import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from .models import User
from .serializers import PublicOneUserSerializer


# Create your views here.
class PublicOneUser(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
        serializer = PublicOneUserSerializer(
            user,
            context={"request": request},
        )
        return Response(serializer.data)


class PublicAllUser(APIView):
    def get(self, request):
        users = User.objects.all()
        if not users.exists():
            raise NotFound("No users found.")
        serializer = PublicOneUserSerializer(
            users, context={"request": request}, many=True
        )
        return Response(serializer.data)
