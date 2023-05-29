# Generated by Django 4.2.1 on 2023-05-29 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('futbol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='jugador_index_page',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='liga_partidos_page',
            name='equipo_local',
            field=models.ForeignKey(choices=[], on_delete=django.db.models.deletion.CASCADE, related_name='equipo_local', to='futbol.equipo'),
        ),
        migrations.AlterField(
            model_name='liga_partidos_page',
            name='equipo_visitante',
            field=models.ForeignKey(choices=[], on_delete=django.db.models.deletion.CASCADE, related_name='equipo_visitante', to='futbol.equipo'),
        ),
    ]