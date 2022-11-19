from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from auth.views import Loginviewset, RegisterView
from users.views import UserViewSet

# from reviews.views import ImageViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'auth/login', Loginviewset, basename='Login')
# router.register(r'register', RegisterView, basename='Register')
router.register(r'users', UserViewSet, basename='Product')
# router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('auth/', include('auth.urls')),
    path('', include(router.urls)),
]
# {
# "username": "username",
# "email":"email",
# "fist_name":"fist_name",
# "last_name":"last_name",
# }

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)