from django.urls import path

from .views import blogs_view

urlpatterns = [
    path("", blogs_view, name="blog")
]
