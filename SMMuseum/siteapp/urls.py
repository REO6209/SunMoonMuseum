from django.urls import path

from siteapp.views import GroupView, GuideDonationView, GuideFacilityView, GuideWatchView, IntroductionHistoryView, MainView, HelloView, RouteView

app_name = "siteapp"

urlpatterns = [
    # 소개
    path('history/', IntroductionHistoryView, name='history'),
    path('main/', MainView, name='main'),
    path('hello/', HelloView, name='hello'),
    path('group/', GroupView, name='group'),
    path('route/', RouteView, name='route'),
    # 안내
    path('guide_facility/', GuideFacilityView, name='guide_facility'),
    path('guide_donation/', GuideDonationView, name='guide_donation'),
    path('guide_watch/', GuideWatchView, name='guide_watch'),
]