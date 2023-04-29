from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
# importamos el modelo de imagenes
from wagtail.images.edit_handlers import ImageChooserPanel
# importamos blog

from blog.models import BlogPageTag
# Create your models here.
'''

Diseña la página base de esta aplicación, que tendrá que recoger al menos la siguiente información:
Nombre completo
Fecha de nacimiento
Lugar de nacimiento (ciudad, país, coordenadas)
Biografía
Fotos
Enlaces a redes sociales
Otros detalles que consideres importantes
'''
class Persona(models.Model):
  nombre = models.CharField(max_length=100)
  apellidos = models.CharField(max_length=100)
  fecha_nacimiento = models.DateField()
  lugar_nacimiento = models.CharField(max_length=100)
  biografia = RichTextField(blank=True)
  # enlace a redes sociales
  twitter = models.CharField(max_length=100, blank=True)
  facebook = models.CharField(max_length=100, blank=True)
  instagram = models.CharField(max_length=100, blank=True)
  # otros detalles
  otros_detalles = RichTextField(blank=True)

  # buscador
  search_fields = Page.search_fields + [
    index.SearchField('nombre'),
    index.SearchField('apellidos'),
    index.SearchField('fecha_nacimiento'),
    index.SearchField('lugar_nacimiento'),
    index.SearchField('biografia'),
    index.SearchField('twitter'),
    index.SearchField('facebook'),
    index.SearchField('instagram'),
    index.SearchField('otros_detalles'),
  ]

  # paneles de administración
  content_panels = Page.content_panels + [
    MultiFieldPanel([
      FieldPanel('nombre'),
      FieldPanel('apellidos'),
      FieldPanel('fecha_nacimiento'),
      FieldPanel('lugar_nacimiento'),
    ], heading="Información personal"),
    FieldPanel('biografia'),
    MultiFieldPanel([
      FieldPanel('twitter'),
      FieldPanel('facebook'),
      FieldPanel('instagram'),
    ], heading="Redes sociales"),
    FieldPanel('otros_detalles'),
  ]

  # plantilla para mostrar
  template = "persona/persona_page.html"

  # para mostrar el nombre completo en el panel de administración
  def __str__(self):
    return self.nombre + ' ' + self.apellidos
        
class PersonaPage(Page):
  date = models.DateField("Post date")
  intro = models.CharField(max_length=250)
  body = RichTextField(blank=True)
  tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

  # ... (Keep the main_image method and search_fields definition)

  content_panels = Page.content_panels + [
    MultiFieldPanel([
      FieldPanel('date'),
      FieldPanel('tags'),
    ], heading="Blog information"),
    FieldPanel('intro'),
    FieldPanel('body'),
  ]
  template = "persona/persona_page.html"
  
  # ...
  
  '''
    Página de listado de personas. Estarán agrupadas y ordenadas por categorías (equipos, o estilos, o categorías, o lo que corresponda)
  '''
class PersonaIndexPage(Page):
        intro = RichTextField(blank=True)

        content_panels = Page.content_panels + [
            FieldPanel('intro')
        ]

        def get_context(self, request):
            # Update context to include only published posts, ordered by reverse-chron
            context = super().get_context(request)
            persona_pages = self.get_children().live().order_by('-first_published_at')
            context['persona_pages'] = persona_pages
            return context

        template = "persona/persona_index_page.html"

        # ...
        # buscador
        search_fields = Page.search_fields + [
            index.SearchField('intro'),
        ]