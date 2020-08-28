from django.contrib import admin
from .models import CustomUser

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth']

admin.site.register(CustomUser, ProfileAdmin)