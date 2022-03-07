from django import forms
from .models import *
from django.forms import ModelForm
from django.forms.widgets import FileInput, Select, TextInput

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class FileRequiredForm(ModelForm):
    class Meta:
        model = FileRequired
        exclude = ['id']
        labels = {
            'file': 'Scegli file',
            'name': 'Nome del file',
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control m-1',
                'type': 'text',
            }),
            'file': FileInput(attrs={
                'class': 'form-control-file',
                'type': 'file',
                'name': 'file',

            }),
        }


class StatusFileForm(ModelForm):
    class Meta:
        model = StatusFile
        exclude = ['file']
        labels = {
            'status': 'STATUS',
        }
        widgets = {
            'status': Select(attrs={
                'class': 'custom-select m-1',
            }),
        }




# class ModelFormWithFileField(ModelForm):
#     class Meta:
#         model = BonusVillaFiles
#         exclude = ['id']
#         labels = {}
#         widgets = {
#             'files': FileInput(attrs={
#                 'class': 'form-control-file',
#                 'type': 'file'
#             }),
#             'images': FileInput(attrs={
#                 'class': 'form-control-file',
#                 'type': 'file'
#             })}