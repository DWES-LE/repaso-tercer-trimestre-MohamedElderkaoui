from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    video = models.FileField( blank=True)
    imagen = models.ImageField( blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('video'),
        FieldPanel('imagen'),
        ]
    subpage_types = ['blog.BlogIndexPage','home.home','persona.PersonaIndex']
    
class home(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    video = models.FileField( blank=True)
    image = models.ImageField( blank=True)
    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        FieldPanel('video'),
        FieldPanel('image'),
        ]
    def __str__(self):
        return self.title