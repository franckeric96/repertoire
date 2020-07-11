from django.contrib import admin
from autres.actions import Action
from . import models 

# Register your models here.



class ContactAdmin(Action):
    list_display = ('nom', 'prenom', 'email')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_enregistrement'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)

