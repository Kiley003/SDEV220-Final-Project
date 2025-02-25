from django.forms import ModelForm
from .models import *
class ApplyForm(ModelForm):
    class Meta:
        model=Routes
        fields="__all__"