from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from django.db import models
from wagtail.search import index
from django.db import models

# New imports added for ClusterTaggableManager, TaggedItemBase, MultiFieldPanel

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from blog.models import BlogPageTag


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
    
class PersonaIndex(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]
    
    subpage_types = ["Persona"]
    
    def personas(self):
        return Persona.objects.live().descendant_of(self)
    
    class Meta:
        verbose_name = "Página de personas"
        verbose_name_plural = "Páginas de personas"
        
    def __str__(self):
        return self.title
class PersonaCategoria(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]
    
    subpage_types = ["Persona"]
    
    def personas(self):
        return Persona.objects.live().descendant_of(self)
    
    class Meta:
        verbose_name = "Página de categorias"
        verbose_name_plural = "Páginas de categorias"
        
    def __str__(self):
        return self.title

# lista de personas
class PersonaList(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        
    ]
    subpage_types = ['Persona']
    def personas(self):
        return Persona.objects.live().descendant_of(self)
    class Meta:
        verbose_name = "Lista de personas"
        verbose_name_plural = "Listas de personas"
    def __str__(self):
        return self.title