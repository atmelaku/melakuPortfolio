from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Images


class UploadImages(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["image", "description"]
        # widgets = {
        #     # Adding a class 'custom-file-input' to target in CSS
        #     'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        # }

class EditImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["image", "description"]
