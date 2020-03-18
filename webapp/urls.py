"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
import knox


urlpatterns = [
    path('', include('apps.frontend.urls', namespace='home')),
    path('boards/', include('apps.board.urls', namespace='board')),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls', namespace='users')), # detail of users
    path('users/accounts/', include('knox.urls')), # detail of users
    # path('accounts/', include('rest_framework.urls')) # login and logout
]