# Generated by Django 4.2.1 on 2023-06-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logos_partidos'),
        ),
    ]
