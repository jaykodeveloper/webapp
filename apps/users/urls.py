from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

app_name="users"

urlpatterns = [
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
]