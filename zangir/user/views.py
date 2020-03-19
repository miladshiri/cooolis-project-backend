from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated


from .serializers import UserSimpleRegisterSerializer
# Create your views here.

UserModel = get_user_model()

class SimpleRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSimpleRegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            new_user = UserModel.objects.create_user(username=username, password=password)

            print (new_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)