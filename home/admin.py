from django.contrib import admin

# Register your models here.
from .models import AnonMessage

class AnonMessageUI(admin.ModelAdmin):
    search_fields = ['time']

admin.site.register(AnonMessage, AnonMessageUI)