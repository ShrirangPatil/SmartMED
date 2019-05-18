from django import forms
from app.choices import MOVEMENTS


class homeForm(forms.Form):
	movements = forms.ChoiceField(choices = MOVEMENTS, label="", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True)

class topologyForm(forms.Form):
	beds = forms.CharField(label='Beds',max_length = 25, help_text = "e.g 1 2")