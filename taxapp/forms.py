from django import forms
from taxapp import models

class NidForm(forms.Form):
    nid = forms.IntegerField(required=True)

class Taxpayer(forms.ModelForm):
    class Meta:
        model = models.Taxpayer
        fields ="__all__"