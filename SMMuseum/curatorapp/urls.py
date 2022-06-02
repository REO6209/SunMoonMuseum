from django.urls import path

from curatorapp.views import BibleDetailView, BibleListView, PermanentDetailView, PermanentListView, SpecialDetailView, SpecialListView

app_name = "curatorapp"

urlpatterns = [
    # 작품 리스트
    path('permanent_list/', PermanentListView.as_view(), name='permanent_list'),
    path('bible_list/', BibleListView.as_view(), name='bible_list'),
    path('special_list/', SpecialListView.as_view(), name='special_list'),
    # 작품 설명
    path('permanent_detail/<int:pk>', PermanentDetailView.as_view(), name='permanent_detail'),
    path('bible_detail/<int:pk>', BibleDetailView.as_view(), name='bible_detail'),
    path('special_detail/<int:pk>', SpecialDetailView.as_view(), name='special_detail'),
]