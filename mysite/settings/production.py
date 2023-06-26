from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# production.py

# Import common settings from base.py
from .base import *

# Set specific production settings
# ...

# Enable multisite
BAKERY_MULTISITE = True

# ...
BAKERY_VIEWS = (
    'wagtailbakery.views.AllPublishedPagesView',
    'wagtailbakery.api_views.PagesAPIDetailView',
    'wagtailbakery.api_views.PagesAPIListingView',
    'wagtailbakery.api_views.TypedPagesAPIListingView',
)