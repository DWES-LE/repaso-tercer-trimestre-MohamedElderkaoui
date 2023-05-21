from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User

# wagtail
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
# ClusterTaggableManager
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from taggit.models import TaggedItemBase, Tag as TaggitTag
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from django import forms
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from blog.models import BlogPage, BlogPageTag
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