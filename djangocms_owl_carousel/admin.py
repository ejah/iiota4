from django.contrib import admin

from .models import OwlStyles

# Register your models here.
@admin.register(OwlStyles)
class OwlStyleAdmin(admin.ModelAdmin):
    pass