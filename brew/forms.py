from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect, SelectMultiple
from brew.models import Brew, Roast, Acidity, Flavor
from django_starfield import Stars

class BrewForm(ModelForm):
	class Meta:
		model = Brew
		exclude = ['user']
		widgets = {
			'roast_levels': RadioSelect(),
			'methods': RadioSelect(),
			'acidity': CheckboxSelectMultiple(),
			'flavor': CheckboxSelectMultiple(),
			'stars': RadioSelect(),
		}

class RoastForm(ModelForm):
	class Meta:
		model = Roast
		exclude = ['user']
		widgets ={
			'roast_levels': RadioSelect(),
		}
		
		

