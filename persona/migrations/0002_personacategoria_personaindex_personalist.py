# Generated by Django 4.1.8 on 2023-05-06 09:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaCategoria',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Página de categorias',
                'verbose_name_plural': 'Páginas de categorias',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PersonaIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Página de personas',
                'verbose_name_plural': 'Páginas de personas',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PersonaList',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Página de listado de personas',
                'verbose_name_plural': 'Páginas de listado de personas',
            },
            bases=('wagtailcore.page',),
        ),
    ]
