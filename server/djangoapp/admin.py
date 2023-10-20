from django.contrib import admin
# from .models import related models
from .models import *

# Register your models here.
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2


# CarModelAdmin class 
class CarModelAdmin(admin.ModelAdmin):
 list_display = ('name', 'cartype', 'year') 
 list_filter = ['year'] 
 search_fields = ['name', 'type'] 
    

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description') 

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
