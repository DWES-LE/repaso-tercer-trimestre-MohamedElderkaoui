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
# Create your models here.
"""Nueva aplicación
La nueva aplicación recogerá información de personas (actores, deportistas, elige el tema) y la mostrará en una página web.

Diseña la página base de esta aplicación, que tendrá que recoger al menos la siguiente información:
Nombre completo
Fecha de nacimiento
Lugar de nacimiento (ciudad, país, coordenadas)
Biografía
Fotos
Enlaces a redes sociales
Otros detalles que consideres importantes
Tienes que crear un modelo para esta información

Página de listado de personas. Estarán agrupadas y ordenadas por categorías (equipos, o estilos, o categorías, o lo que corresponda)

Diseño de las plantillas de detalle de las personas y del listado general
    """
    
class Persona(Page):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    biografia = RichTextField()
    foto = models.ImageField(upload_to="persona")
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    body = RichTextField(blank=True)
    into = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    
    template = "persona/persona_page.html"
    search_fields = Page.search_fields + [
        index.SearchField("nombre"),
        index.SearchField("apellidos"),
        index.SearchField("fecha_nacimiento"),
        index.SearchField("lugar_nacimiento"),
        index.SearchField("biografia"),
        index.SearchField("twitter"),
        index.SearchField("facebook"),
        index.SearchField("instagram"),
        index.SearchField("linkedin"),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel("nombre"),
        FieldPanel("apellidos"),
        FieldPanel("fecha_nacimiento"),
        FieldPanel("lugar_nacimiento"),
        FieldPanel("biografia"),
        FieldPanel("foto"),
        FieldPanel("twitter"),
        FieldPanel("facebook"),
        FieldPanel("instagram"),
        FieldPanel("linkedin"),
    ]
    
    promote_panels = Page.promote_panels + [
        FieldPanel("body"),
        FieldPanel("into"),
    ]
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        
    def __str__(self):
        return self.nombre + " " + self.apellidos

class PersonaIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]
    template = "persona/persona_list_page.html"
    
    subpage_types = ["Persona"]
    def get_context(self, request):
        context = super().get_context(request)
        personas = self.get_children().live().order_by("-first_published_at")
        context["personas"] = personas
        return context
    
    class Meta:
        verbose_name = "Página de índice de personas"
        verbose_name_plural = "Páginas de índice de personas"
        
    def __str__(self):
        return self.title