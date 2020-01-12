from django.contrib import admin
from django.urls import path, include
from dataservice import views

urlpatterns = [
    path("send-emails", views.send_emails, name='send_emails'),
    path("create-scam-emails", views.create_scam_emails, name='create_scam_emails'),
    path("create-potential-scam-emails", views.create_potential_scam_emails, name='create_potential_scam_emails'),
    path("get_every_scam_email", views.get_every_scam_email, name='get_every_scam_email'),
    path("", views.index, name="index")
]