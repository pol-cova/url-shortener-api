from django.forms import ModelForm
from .models import Url

# UrlForm
class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url']
