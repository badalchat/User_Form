from django.contrib import admin
from app.models import RegForm


class RegFormAdmin(admin.ModelAdmin):
    list_display = ["Name", "DoB", "Email", "Phone"]


# Register your models here.
admin.site.register(RegForm, RegFormAdmin)
