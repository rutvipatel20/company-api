from django.contrib import admin
from home.models import Color,Person
# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    list_display=('color_name',)
    
class PersonAdmin(admin.ModelAdmin):
    list_display=('name','age','color')

admin.site.register(Color,ColorAdmin)
admin.site.register(Person,PersonAdmin)
