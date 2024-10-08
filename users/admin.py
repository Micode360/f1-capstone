from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name','is_staff')
    search_fields = ('id','email', 'first_name', 'last_name')

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)