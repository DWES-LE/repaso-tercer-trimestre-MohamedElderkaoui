from django.shortcuts import render

# Create your views here.
from wagtail.admin.viewsets.model import ModelViewSet
from .models import Person


class PersonViewSet(ModelViewSet):
    model = Person
    form_fields = ["first_name", "last_name"]
    icon = "user"


person_viewset = PersonViewSet("person")  # defines /admin/person/ as the base URL