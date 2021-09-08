from django import forms
from .models import *


class UploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'