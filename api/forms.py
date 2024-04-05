from django.forms import ModelForm, Form, TextInput
from .models import Url

# UrlForm
class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url']

        # form-control class for the input field
        widgets = {
            'url': TextInput(attrs={'class': 'form-control'}),
        }

