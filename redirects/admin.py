from django.contrib import admin
from .models import Redirect
# Register your models here.

@admin.register(Redirect)
class RedirectsAdmin(admin.ModelAdmin):
    list_display = ("key", "url", "active")