from django.shortcuts import render
from .models import (
    BaseContent,
    Contact,
    Service,
    ServiceField,
    Career,
    CareerField,
    PortFolio,
)

# Create your views here.
def index(request):
    base = BaseContent.objects.all()
    context = {
        "base": base,
    }
    return render(request, "pe/index.html", context)


def service_view(request):
    service = Service.objects.all()
    return render(request, "pe/services.html", {"services": service,})


def career_view(request):
    career = Career.objects.all()

    return render(request, "pe/career.html", {"careers": career,})


def portfo(request):
    pf = PortFolio.objects.all()
    return render(request, "pe/portfo.html", {"portfolio": pf})


def about(request):
    about = BaseContent.objects.all()
    return render(request, "pe/about.html", {"about": about})


def contact_view(request):
    contact = Contact.objects.all()
    context = {
        "contact": contact,
    }
    return render(request, "pe/contact.html", context)


def respond_view(request):
    return render(request, "pe/career.html",)


def respond_view(request):
    return render(request, "pe/respond.html",)
