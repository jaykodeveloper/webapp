from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import index

# board/urls.py
app_name = 'frontend'
urlpatterns = [
    path('', index, name="main"),
]
urlpatterns = format_suffix_patterns(urlpatterns)