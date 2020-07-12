from django.db import models
from tinymce import HTMLField

# Create your models here.
class SocialAccount(models.Model):
    ICONS = [
        ("facebook", "fa fa-facebook"),
        ("instagram", "fa fa-instagram"),
        ("google-plus", "fa-google-plus-g"),
        ("linkedin", "fa-linkedin-in"),
        ("twitter", "fa fa-twitter")
    ]
    
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials account'

    def __str__(self):
        return self.nom


class Presentation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    slogan = models.TextField()
    logo = models.ImageField(upload_to="images/Presentation", null=True)
    image = models.ImageField(upload_to="images/Presentation")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.nom

class Gallerie(models.Model):

    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/gallerie")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Gallerie'
        verbose_name_plural = 'Galleries'

    def __str__(self):
       return self.nom



class Article(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField()
    contenu = HTMLField()
    image_article = models.ForeignKey(Gallerie, verbose_name= "image article", on_delete=models.CASCADE)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre
