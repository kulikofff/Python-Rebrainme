from django.contrib import admin

from .models import Server

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'description', 'server_is_active', 'data_active')