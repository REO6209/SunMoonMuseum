from django.shortcuts import render
from django.views.generic import DetailView, ListView

from curatorapp.models import Bible, Permanent, Special

# Create your views here.
# 작품 리스트
class PermanentListView(ListView):
    model = Permanent
    context_object_name = 'permanent_list'
    template_name = 'curatorapp/permanent_list.html'
    paginate_by = 4


class BibleListView(ListView):
    model = Bible
    context_object_name = 'bible_list'
    template_name = 'curatorapp/bible_list.html'
    paginate_by = 4


class SpecialListView(ListView):
    model = Special
    context_object_name = 'special_list'
    template_name = 'curatorapp/special_list.html'
    paginate_by = 4


# 작품 설명
class PermanentDetailView(DetailView):
    model = Permanent
    context_object_name = 'target_permanent'
    template_name = 'curatorapp/permanent_detail.html'


class BibleDetailView(DetailView):
    model = Bible
    context_object_name = 'target_bible'
    template_name = 'curatorapp/bible_detail.html'


class SpecialDetailView(DetailView):
    model = Special
    context_object_name = 'target_special'
    template_name = 'curatorapp/special_detail.html'