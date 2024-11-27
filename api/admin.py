from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_id','name','location','about','type','is_active')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','address','phone','about','position','company','is_active')

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)