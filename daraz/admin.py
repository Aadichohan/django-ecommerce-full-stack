from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display  = ("username", "email", "name", "is_active", "created_at", "updated_at")
    search_fields = ('username', 'email', 'name')
admin.site.register(User, UserAdmin)