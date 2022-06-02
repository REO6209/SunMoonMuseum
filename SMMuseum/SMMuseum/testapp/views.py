from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView, DetailView
from testapp.forms import TestCreationForm

from testapp.models import TestOCR


# Create your views here.
class TestOCRCreateView(CreateView):
    model = TestOCR
    context_object_name = 'target_info'
    form_class = TestCreationForm
    template_name = 'testapp/create.html'
    
    def get_success_url(self):
        return reverse('testapp:detail', kwargs={'pk': self.object.pk})


class TestOCRDetailView(DetailView):
    model = TestOCR
    context_object_name = 'target_info'
    template_name = 'testapp/detail.html'