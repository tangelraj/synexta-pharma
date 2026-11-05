from django.urls import path
from . import views

urlpatterns = [
    path("submit-enquiry/", views.submit_enquiry, name="submit_enquiry"),
    path("home/", views.home_data, name="home_data"),
    path("about/", views.about_data, name="about_data"),
    path("products/", views.products_data, name="products_data"),
    path("contact/", views.contact_data, name="contact_data"),
]