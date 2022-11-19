from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import ItemSerializer


class ItemViewSet(ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        serializer = Serializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

class ItemModelViewSet(ViewSet):
    serializer_class = ItemSerializer
    queryset = User.objects.all()


class UserViewSet(ViewSet):
    def list(self, request):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        items = User.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = {
            "title": request.POST.get('title', None),
            }
        serializer = self.serializer_class(data=data, # or request.data
                                        context={'author': user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
