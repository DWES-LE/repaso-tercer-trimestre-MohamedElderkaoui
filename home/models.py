from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from persona.models import PersonaIndexPage
from blog.models import BlogIndexPage
from futbol.models import Equipo_index
from politica.models import Eleccion

class HomePage(Page):
    body = RichTextField(blank=True)
    
    subpage_types = [ PersonaIndexPage, BlogIndexPage ,Equipo_index,Eleccion ]
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]