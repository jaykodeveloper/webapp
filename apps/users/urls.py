from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views
from .views import (
    UserList, UserDetail, api_root, RegistrationAPI, LoginAPI
)
import knox


app_name = 'users'
urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('accounts/register/', RegistrationAPI.as_view(), name='user-register'),
    path('accounts/login/', LoginAPI.as_view(), name='user-login'),
    path('accounts/logout/', knox_views.LogoutView.as_view(), name='user-logout'),
    path('accounts/user', UserDetail.as_view(), name='user-individual')
]

urlpatterns = format_suffix_patterns(urlpatterns)