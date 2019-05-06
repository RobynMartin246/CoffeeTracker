from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect, SelectMultiple
from brew.models import Brew, Roast, Acidity, Flavor

class BrewForm(ModelForm):
	class Meta:
		model = Brew
		exclude = ['user']
		widgets = {
			'roast_levels': RadioSelect(),
			'methods': RadioSelect(),
			'acidity': CheckboxSelectMultiple(),
			'flavor': CheckboxSelectMultiple()
		}

class RoastForm(ModelForm):
	class Meta:
		model = Roast
		fields = '__all__'
		widgets ={
			'roast_levels': RadioSelect(),
		}
		
		

