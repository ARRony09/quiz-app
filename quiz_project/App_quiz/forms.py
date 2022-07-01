from dataclasses import fields
from django.forms import ModelForm
from .models import QuesModel

class addQuestion(ModelForm):
    class Meta:
        model=QuesModel
        fields='__all__'