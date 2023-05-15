'''
py manage.py shell < bp.py

'''
from wagtail.core.models import Page
Page.objects.all().delete()