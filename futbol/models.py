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


class jugador(Page):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    numero = models.IntegerField()
    imagen = models.ImageField(upload_to='images/')
    contenido = RichTextField(blank=True)
    #equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    parent_page_types = ['Equipo']
    subpage_types = []
    template = "futbol/jugador_page.html"
    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('apellido'),
        FieldPanel('numero'),
        FieldPanel('imagen'),
        FieldPanel('contenido'),
       # FieldPanel('equipo'),
    ]


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






