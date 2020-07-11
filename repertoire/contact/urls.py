from django.urls import path
from . import views

urlpatterns = [
  
    path("contacts/", views.contact_list, name="contacts"),
    path("contacts/<int:id>/", views.contact_details, name="details"),
    path("contacts/new/", views.new_contact, name="new_contact"),
    path("contacts/edit/<int:id>/", views.edit_contact, name="edit_contact"),
    path("contacts/delete/<int:id>/", views.delete_contact, name="delete_contact")

 


    
]