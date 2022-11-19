from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status, viewsets
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.validators import UniqueValidator
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ItemSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token

class CreateViewset(viewsets.ViewSet):
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

class UserViewSet(ViewSet):
    serializer_class = ItemSerializer
    queryset = User.objects.all()
    permission_classes = [DjangoObjectPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)