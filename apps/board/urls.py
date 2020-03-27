from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BoardList, BoardDetail, api_root

app_name = 'board'
urlpatterns = [
    path('', BoardList.as_view(), name='board-list'),
    path('<int:pk>/', BoardDetail.as_view(), name='board-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)