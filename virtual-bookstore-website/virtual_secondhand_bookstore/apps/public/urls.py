from django.urls import path

from . import views

# import from local directory

# public:index public calling index
app_name = "public"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
