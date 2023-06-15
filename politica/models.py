
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
#  base de dato de elecciones politicas españolas


# para usar chartjs

class Eleccion(Page):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = RichTextField()
    numero_votos = models.IntegerField(default=0)
    region_pueblo_comunidad = models.CharField(max_length=100)
   
    
    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('fecha'),
        FieldPanel('descripcion'),
        FieldPanel('region_pueblo_comunidad'),
        FieldPanel('numero_votos'),
        
    ]

    def __str__(self):
        return self.nombre
    template = "politica/eleccion_page.html"
    subpage_types = ['Partido']
class Partido(Page):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    lider = models.CharField(max_length=100)
    descripcion = RichTextField()
    numero_votos = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='logos_partidos', blank=True)

    
    template = "politica/partido_page.html"

    content_panels = Page.content_panels + [
        FieldPanel('nombre'),
        FieldPanel('fundacion'),
        FieldPanel('lider'),
        FieldPanel('descripcion'),
        FieldPanel('numero_votos'),
        FieldPanel('logo'),
    ]
    
class Lista_Eleccion(Page):
    subpage_types = [Eleccion]
    template = "politica/lista_eleccion_page.html"
            