# Generated by Django 4.1.8 on 2023-05-08 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='image',
            new_name='imagen',
        ),
    ]
