from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone', 'is_read')
    list_filter = ('email', 'username', 'phone')
    search_fields = ('email', 'username')