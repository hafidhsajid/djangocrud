from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (LoginSerializer, MyTokenObtainPairSerializer,
                          RegisterSerializer)


class Loginviewset(viewsets.ViewSet):
    def list(self, request):
        permission_classes = (AllowAny,)
        serializer_class = LoginSerializer
    
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# class RegisterView(generics.CreateAPIView):
class RegisterView(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        permission_classes = (AllowAny,)
        serializer_class = RegisterSerializer
        return Response(serializer_class, status=status.HTTP_200_OK)

    # @classmethod
    # def get_extra_actions(cls):
    #     permission_classes = (AllowAny,)
    #     serializer_class = RegisterSerializer

# class RegisterView(viewsets.ViewSet):
#     def list(self, request):
#         queryset = User.objects.all()
#         permission_classes = (AllowAny,)
#         serializer_class = RegisterSerializer