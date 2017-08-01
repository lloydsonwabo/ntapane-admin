from django.contrib import admin
from django.utils.translation import ugettext_lazy

# Register your models here.
from .models import Client

class ClientAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Surname', 'Id_Number','Employer', 'Employee_Number', 'Income', 'Premium', 'Policy_type', 'Street', 'City', 'Postal_Code', 'Cell_Number', 'Created')
	list_filter = ('Created', 'Surname')
	search_fields = ('Name', 'Surname', 'Id_Number')
    

admin.site.register(Client, ClientAdmin)

admin.site.site_header = 'Ntapane Administration'
