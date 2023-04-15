from django.contrib import admin
from django.http import JsonResponse
# import FieldPanel
from wagtail.admin.edit_handlers import FieldPanel
# import InlinePanel
from wagtail.admin.edit_handlers import InlinePanel

# Register your models here.
content_panels = [
    FieldPanel('title', classname="full title"),    
    InlinePanel('related_links', label="Related links"),
]