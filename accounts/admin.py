from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'registered_on']
    search_fields = ['user__username', 'user__email']


