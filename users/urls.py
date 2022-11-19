from django.urls import include, path
from rest_framework import routers

from .views import ItemModelViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'get', UserViewSet, basename="userviewset")
router.register(r'model-viewset', ItemModelViewSet)

urlpatterns = [
    # path('change-user-info', ChangeUserInfo.as_view()),
    # path('create', CreateViewset),
    path('', include(router.urls)),
]