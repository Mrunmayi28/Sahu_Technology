from django.contrib import admin
from .models import details

# Register your models here.

@admin.register(details)
class Admindetails(admin.ModelAdmin):
    list_display = ('Fname','Lname','Email','Number','Dname','Branch','Dscore','Styear','Dyear','Hsc','Hscore',
                    'Hyear','Ssc','Sscore','Syear','Experience','Skills','Awards')