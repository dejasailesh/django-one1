from django.contrib import admin
from .models import BaseContent, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "myemail",
        "myphn",
        "myadd",
    )


admin.site.register(BaseContent)
admin.site.register(Contact, ContactAdmin)

