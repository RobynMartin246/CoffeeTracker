from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect, SelectMultiple
from brew.models import Brew, Roast, Acidity, Flavor


class BrewForm(ModelForm):
	class Meta:
		model = Brew
		fields='__all__'
		widgets = {
			'roast_levels': RadioSelect(),
			'methods': RadioSelect(),
			'acidity': CheckboxSelectMultiple(),
			'flavor': CheckboxSelectMultiple(),
			'stars': RadioSelect(),
		}
	def __init__(self, user, *args, **kwargs):
		super(BrewForm, self).__init__(*args, **kwargs)
		self.fields['home_roast'].queryset = Roast.objects.filter(user=user)

class RoastForm(ModelForm):
	class Meta:
		model = Roast
		exclude = ['user']
		widgets ={
			'roast_levels': RadioSelect(),
		}



