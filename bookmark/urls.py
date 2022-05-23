# config에 있는 urls를 쓰지않는 이유는 재활용이 어려워서이다. 이렇게 별도로 생성하여 추후 config에 pathfh 연결시켜주면 된다
from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]
