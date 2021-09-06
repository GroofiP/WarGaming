from django import forms

from viewdowapp.models import FormDownload


class TextDownloadForm(forms.ModelForm):
    class Meta:
        model = FormDownload
        fields = ("text_file",)
