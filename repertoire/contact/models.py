from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):

    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, null=True, blank=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)

    class Meta:
        verbose_name ="contact"
        verbose_name_plural ="contacts"


    def __str__(self):
        return f"{self.nom} {self.prenom}"