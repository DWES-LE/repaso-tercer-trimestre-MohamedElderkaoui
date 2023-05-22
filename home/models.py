from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from persona.models import PersonaIndexPage
from blog.models import BlogIndexPage

class HomePage(Page):
    body = RichTextField(blank=True)
    
    subpage_types = [ PersonaIndexPage, BlogIndexPage ]
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]