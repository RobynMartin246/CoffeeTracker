from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Brew, Roast, Acidity, Flavor

class BrewAdmin(admin.ModelAdmin):
	fields = [
		'coffee_name',
		'roastery',
		'pub_date',  
		'roast_levels',
		'home_roast'
		'user',
		'methods', 
		'flavor',
		'acidity'
		
		

	]
	list_display = ('coffee_name', 'user', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['coffee_name']

admin.site.register(Brew, BrewAdmin)

class RoastAdmin(admin.ModelAdmin):
	fields = [
		'origin',
		'roast_name',
		'roast_time',
		'batch_size',
		'roast_levels',
		'first_crack_start',
		'first_crack_end',
		'second_crack_start',
		'notes'
		]
	list_display = ('roast_name', 'origin', 'user', 'pub_date')


admin.site.register(Roast, RoastAdmin)

class AcidityAdmin(admin.ModelAdmin):
	fields = ['acidity']

admin.site.register(Acidity, AcidityAdmin)

class FlavorAdmin(admin.ModelAdmin):
	fields = ['flavor']

admin.site.register(Flavor, FlavorAdmin)


# Register your models here.
