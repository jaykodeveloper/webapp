from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, api_root

# from .views import BoardList, BoardCreate, BoardDelete, BoardDetail, BoardUpdate

app_name = 'users'
urlpatterns = [
    path('list/', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('', api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)