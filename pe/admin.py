from django.contrib import admin
from .models import (
    BaseContent,
    Contact,
    Service,
    Career,
    ServiceField,
    CareerField,
    PortFolio,
)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "myemail",
        "myphn",
        "myadd",
    )


admin.site.register(Service)
admin.site.register(Career)
admin.site.register(ServiceField)
admin.site.register(CareerField)
admin.site.register(BaseContent)
admin.site.register(Contact, ContactAdmin)
admin.site.register(PortFolio)
