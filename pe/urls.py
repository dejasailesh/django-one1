from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_page"),
    path("services/", views.service_view, name="service_page"),
    path("about/", views.about, name="about_page"),
    path("portfolio/", views.portfo, name="portfolio_page"),
    path("career/", views.index, name="career_page"),
    path("contact/", views.contact_view, name="contact_page"),
]
