from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    video = models.FileField( blank=True)
    image = models.ImageField( blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('video'),
        FieldPanel('image'),
        ]