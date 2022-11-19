from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from auth.views import Loginviewset, MyObtainTokenPairView, RegisterView

router = routers.DefaultRouter()
# router.register(r'login', MyObtainTokenPairView, basename="login")
router.register(r'register', RegisterView, basename="register")
# router.register(r'register', RegisterView.as_view(), basename="register")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterView.as_view() , name='auth_register'),
]
# path('', include(urlpatterns)),