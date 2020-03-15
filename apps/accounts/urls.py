from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail 

# from .views import BoardList, BoardCreate, BoardDelete, BoardDetail, BoardUpdate

app_name = 'accounts'
urlpatterns = [
    path('list/', UserList.as_view(), name='userlist'),
    path('<int:pk>/', UserDetail.as_view(), name='userdetail'),
]