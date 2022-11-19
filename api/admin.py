from django.contrib import admin
from . models import Application



# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    
    List_display = ('name', 'address', 'city')


admin.site.register(Application, ApplicationAdmin)
