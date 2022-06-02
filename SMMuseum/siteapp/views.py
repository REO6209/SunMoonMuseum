from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from SMMuseum import settings

from siteapp.models import Introduction_history


# Create your views here.
def IntroductionHistoryView(request):
    history = Introduction_history.objects
    template = loader.get_template('siteapp/history.html')
    context = {
        'history': history,
    }
    return HttpResponse(template.render(context, request))

def MainView(request):
    return render(request, 'siteapp/main.html')

def HelloView(request):
    return render(request, 'siteapp/hello.html')

def GroupView(request):
    return render(request, 'siteapp/group.html')

def RouteView(request):
    template = loader.get_template('siteapp/route.html')
    context = {
        'api_key': settings.KAKAO_MAP_API_KEY
    }
    return HttpResponse(template.render(context, request))

def GuideFacilityView(request):
    return render(request, 'siteapp/guide_facility.html')

def GuideDonationView(request):
    return render(request, 'siteapp/guide_donation.html')

def GuideWatchView(request):
    return render(request, 'siteapp/guide_watch.html')