# Generated by Django 2.2.10 on 2020-07-11 19:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_presentation_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=tinymce.models.HTMLField(),
        ),
    ]
