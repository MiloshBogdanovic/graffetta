from django import forms
from .models import *
from django.forms import ModelForm
from django.forms.widgets import FileInput


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ModelFormWithFileField(ModelForm):
    class Meta:
        model = BonusVillaFiles
        exclude = ['id']
        labels = {}
        widgets = {
            'files': FileInput(attrs={
                'class': 'form-control-file',
                'type': 'file'
            }),
            'images': FileInput(attrs={
                'class': 'form-control-file',
                'type': 'file'
            })}