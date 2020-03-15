from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BoardList, BoardDetail

# from .views import BoardList, BoardCreate, BoardDelete, BoardDetail, BoardUpdate

app_name = 'board'
urlpatterns = [
    path('', BoardList.as_view(), name='index'),
    path('<int:pk>', BoardDetail.as_view(), name='rest'),
]
"""
urlpatterns = [
    path('', BoardList.as_view(), name='index'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('delete/<int:pk>', BoardDelete.as_view(), name='delete'),
    path('update/<int:pk>', BoardUpdate.as_view(), name='update'),
    path('detail/<int:pk>', BoardDetail.as_view(), name='detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""