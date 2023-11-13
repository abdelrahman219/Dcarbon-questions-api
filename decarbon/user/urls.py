from django.urls import path
from .views import CreateUserView, CreateTokenView, ManageUserView, get_user_id, logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    # path('token/', CreateTokenView.as_view(), name='token_obtain_pair'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', ManageUserView.as_view(), name='me'),
    path('userid/', get_user_id, name='get_user_id'),
    path('logout/', logout, name='logout'),
]
