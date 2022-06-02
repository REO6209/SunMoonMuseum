from django.forms import ModelForm

from testapp.models import TestOCR


class TestCreationForm(ModelForm):
    class Meta:
        model = TestOCR
        fields = ['title', 'image']