from django.db import models

# Page of wagtail
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import DateField
from django.db.models.fields import TextField
from django.db.models.fields import URLField

from django.db.models.fields.related import ManyToManyField

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from blog.models import BlogPageTag



# Create your models here.

class Equipo(Page):# listado de jugadores, entrenadores, etc y partidos , partidos jugados, ganados, perdidos, etc
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='images/')
    contenido = RichTextField(blank=True)
    subpage_types = ['jugador', 'entrenador']
    template = "futbol/equipo_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('imagen'),
        FieldPanel('contenido'),
        #FieldPanel('jugadores'),
        #FieldPanel('partidos'),
    ]
class Equipo_index(Page):# listado de jugadores, entrenadores, etc y partidos , partidos jugados, ganados, perdidos, etc
    subpage_types = ['Equipo']
    template = "futbol/equipo_index_page.html"
    def save(self, *args, **kwargs):
        e = self.get_children().type(Equipo).all()
        for equipo in e:
            equipo.save()   

class jugador(Page):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    numero = models.IntegerField()
    edad = models.IntegerField(default=18)
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')))
    imagen = models.ImageField(upload_to='images/')
    #equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    parent_page_types = ['Equipo']
    subpage_types = []
    template = "futbol/jugador_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('apellido'),
        FieldPanel('numero'),
        FieldPanel('imagen'),
        FieldPanel('edad'),
       # FieldPanel('equipo'),
    ]
    def save(self, *args, **kwargs):
        # Calculate the points based on the results
        self.numero = self.numero + 1

        # Save the instance
        super().save(*args, **kwargs)

class jugador_index_page(Page):
    subpage_types = ['jugador']
    template = "futbol/jugador_index_page.html"
    
class entrenador(Page):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='images/')
    contenido = RichTextField(blank=True)
    #equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    parent_page_types = ['Equipo']
    subpage_types = []
    template = "futbol/entrenador_page.html"

    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('apellido'),
        FieldPanel('imagen'),
        FieldPanel('contenido'),
        #FieldPanel('equipo'),
    ]
class entrenador_index_page(Page):
    subpage_types = ['entrenador']
    template = "futbol/entrenador_index_page.html"

class Liga_Partidos_Page(Page):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_local', choices=Equipo.objects.all())
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_visitante', choices=Equipo.objects.all())
    fecha = models.DateField()
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    parent_page_types = ['Liga_Clasificacion_Page']
    subpage_types = []
    template = "futbol/liga_partidos_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('equipo_local'),
        FieldPanel('equipo_visitante'),
        FieldPanel('fecha'),
        FieldPanel('goles_local'),
        FieldPanel('goles_visitante'),
    ]
    def save(self, *args, **kwargs):
        # Custom logic or calculations before saving
        # For example, updating the result based on the goals scored
        if self.goles_local > self.goles_visitante:
            self.resultado = 'Local'
        elif self.goles_local < self.goles_visitante:
            self.resultado = 'Visitante'
        else:
            self.resultado = 'Empate'

        # Save the instance
        super().save(*args, **kwargs)

class Liga_Clasificacion_Page(Page):
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='images/')
    contenido = RichTextField(blank=True)
    equipos = models.ManyToManyField(Equipo)
    puntos = models.IntegerField()
    partidos_jugados = models.IntegerField()
    partidos_ganados = models.IntegerField()
    partidos_empatados = models.IntegerField()
    partidos_perdidos = models.IntegerField()
    goles_favor = models.IntegerField()
    goles_contra = models.IntegerField()
    subpage_types = ['Equipo']
    template = "futbol/liga_clasificacion_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('imagen'),
        FieldPanel('contenido'),
        FieldPanel('equipos'),
        FieldPanel('puntos'),
        FieldPanel('partidos_jugados'),
        FieldPanel('partidos_ganados'),
        FieldPanel('partidos_empatados'),
        FieldPanel('partidos_perdidos'),    
        FieldPanel('goles_favor'),
        FieldPanel('goles_contra'),
    ]
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first to ensure it has an ID

        # Iterate through all the matches (child pages of type Liga_Partidos_Page)
        matches = self.get_children().type(Liga_Partidos_Page)
        for match in matches:
            equipo_local = match.equipo_local
            equipo_visitante = match.equipo_visitante
            goles_local = match.goles_local
            goles_visitante = match.goles_visitante

            # Update the teams' statistics based on the match result
            equipo_local.partidos_jugados += 1
            equipo_visitante.partidos_jugados += 1

            if goles_local > goles_visitante:
                equipo_local.partidos_ganados += 1
                equipo_local.puntos += 3
                equipo_visitante.partidos_perdidos += 1
            elif goles_local < goles_visitante:
                equipo_visitante.partidos_ganados += 1
                equipo_visitante.puntos += 3
                equipo_local.partidos_perdidos += 1
            else:
                equipo_local.partidos_empatados += 1
                equipo_local.puntos += 1
                equipo_visitante.partidos_empatados += 1
                equipo_visitante.puntos += 1

            # Update goals scored and goals conceded
            equipo_local.goles_favor += goles_local
            equipo_local.goles_contra += goles_visitante
            equipo_visitante.goles_favor += goles_visitante
            equipo_visitante.goles_contra += goles_local

            # Save the updated teams
            equipo_local.save()
            equipo_visitante.save()

class Liga_Index_Page(Page):
    subpage_types = ['Liga_Clasificacion_Page']
    template = "futbol/liga_index_page.html"
    
class partido(Page):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_local_partido', choices=Equipo.objects.all())
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_visitante_partido', choices=Equipo.objects.all())
    fecha = models.DateField()
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    parent_page_types = ['Equipo']
    subpage_types = []
    template = "futbol/partido_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('equipo_local'),
        FieldPanel('equipo_visitante'),
        FieldPanel('fecha'),
        FieldPanel('goles_local'),
        FieldPanel('goles_visitante'),
    ]
    def save(self, *args, **kwargs):
        # Custom logic or calculations before saving
        # For example, updating the result based on the goals scored
        if self.goles_local > self.goles_visitante:
            self.resultado = 'Local'
        elif self.goles_local < self.goles_visitante:
            self.resultado = 'Visitante'
        else:
            self.resultado = 'Empate'

        # Save the instance
        super().save(*args, **kwargs)