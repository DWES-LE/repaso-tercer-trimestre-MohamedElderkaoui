from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from django.db import models
# ParentalKey
from modelcluster.fields import ParentalKey

class Persona(Page):
  body = RichTextField(blank=True)
  fecha_nacimiento = models.DateField()
  lugar_nacimiento = models.CharField(max_length=255)
  coordenadas = models.CharField(max_length=255)
  biografia = RichTextField(blank=True)
  fotos = InlinePanel('Persona_fotos', label="Fotos")
  redes_sociales = InlinePanel('Persona_redes_sociales', label="Redes sociales")
  
  template = "persona_page.html"
  content_panels = Page.content_panels + [
  FieldPanel('fecha_nacimiento'),
  FieldPanel('lugar_nacimiento'),
  FieldPanel('coordenadas'),
  FieldPanel('biografia', classname="full"),
  InlinePanel('fotos', label="Fotos"),
  InlinePanel('redes_sociales', label="Redes sociales"),
  ]

class Persona_fotos(models.Model):
  page = ParentalKey(Persona, on_delete=models.CASCADE, related_name='fotos')
  foto = models.ForeignKey(
  'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
  )
  panels = [
  ImageChooserPanel('foto')
  ]

class Persona_redes_sociales(models.Model):
  page = ParentalKey(Persona, on_delete=models.CASCADE, related_name='redes_sociales')
  nombre = models.CharField(max_length=255)
  enlace = models.URLField()
  panels = [
  FieldPanel('nombre'),
  FieldPanel('enlace'),
  ]