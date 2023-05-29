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
class liga(Page):
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='images/')
    contenido = RichTextField(blank=True)
    subpage_types = ['equipo']
    template = "futbol/liga_page.html"
    
    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('imagen'),
        FieldPanel('contenido'),
    ]

class equipo(Page):# listado de jugadores, entrenadores, etc y partidos , partidos jugados, ganados, perdidos, etc
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

class jugador(Page):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    numero = models.IntegerField()
    imagen = models.ImageField(upload_to='images/')
    contenido = RichTextField(blank=True)
    equipo = models.ForeignKey('equipo', on_delete=models.CASCADE)
    parent_page_types = ['equipo']
    subpage_types = []
    template = "futbol/jugador_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('apellido'),
        FieldPanel('numero'),
        FieldPanel('imagen'),
        FieldPanel('contenido'),
    ]


class entrenador(Page):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='images/')
    contenido = RichTextField(blank=True)
    equipo = models.ForeignKey('equipo', on_delete=models.CASCADE)
    parent_page_types = ['equipo']
    subpage_types = []
    template = "futbol/entrenador_page.html"

    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('apellido'),
        FieldPanel('imagen'),
        FieldPanel('contenido'),
    ]
    
class partido(Page):
    equipo1 = models.ForeignKey('equipo', on_delete=models.CASCADE, related_name='equipo1')
    equipo2 = models.ForeignKey('equipo', on_delete=models.CASCADE, related_name='equipo2')
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=250)
    goles_equipo1 = models.IntegerField()
    goles_equipo2 = models.IntegerField()
    
    parent_page_types = ['equipo']
    subpage_types = []
    template = "futbol/partido_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('equipo1'),
        FieldPanel('equipo2'),
        FieldPanel('fecha'),
        FieldPanel('hora'),
        FieldPanel('lugar'),
    ]
    def __save__(self, *args, **kwargs):
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        super(partido, self).save(*args, **kwargs)


    





