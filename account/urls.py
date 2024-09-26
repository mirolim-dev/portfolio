from django.urls import path

from .views import (
    home, about, services_view, contact_view,
    )

urlpatterns = [
    path("", home, name="home"), 
    path("about/", about, name="about"),   
    path("services/", services_view, name="services"),
    path("contact/", contact_view, name="contact"),
]
