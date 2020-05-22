from django.shortcuts import render
from .models import BaseContent, Contact

# Create your views here.
def index(request):
    base = BaseContent.objects.all()
    context = {
        "base": base,
    }
    return render(request, "pe/base.html", context)


def service_view(request):
    return render(request, "pe/services.html",)


def portfo(request):
    return render(request, "pe/portfo.html",)


def about(request):
    return render(request, "pe/about.html",)


def contact_view(request):
    contact = Contact.objects.all()
    context = {
        "contact": contact,
    }
    return render(request, "pe/contact.html", context)
