from django.urls import path

from testapp.views import TestOCRCreateView, TestOCRDetailView

app_name = "testapp"

urlpatterns = [
    path('create/', TestOCRCreateView.as_view(), name='create'),
    path('detail/<int:pk>', TestOCRDetailView.as_view(), name='detail'),
]