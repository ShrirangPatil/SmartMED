from django import forms
from app.choices import MOVEMENTS


class homeForm(forms.Form):
	movements = forms.ChoiceField(choices = MOVEMENTS, label="", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True)