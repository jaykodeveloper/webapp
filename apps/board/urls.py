from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BoardList, BoardDetail, api_root

# board/urls.py
app_name = 'board'
urlpatterns = [
    path('boards/', BoardList.as_view(), name='board-list'),
    path('boards/<int:pk>/', BoardDetail.as_view(), name='board-detail'),
    path('', api_root),
]
urlpatterns = format_suffix_patterns(urlpatterns)