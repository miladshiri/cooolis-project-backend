from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import SimpleRegistrationView

app_name = "user"

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('simple-registration', SimpleRegistrationView.as_view(), name='simple_registration')
]