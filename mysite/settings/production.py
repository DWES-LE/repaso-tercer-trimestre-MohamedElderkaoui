from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


BAKERY_MULTISITE = True

BUILD_DIR = '/tmp/build/'

BAKERY_VIEWS = (
	'wagtailbakery.views.AllPublishedPagesView',
)
BAKERY_VIEWS = (
	'wagtailbakery.views.AllPagesView',
)
BAKERY_VIEWS = (
	'wagtailbakery.api_views.PagesAPIDetailView',
	'wagtailbakery.api_views.PagesAPIListingView',
	'wagtailbakery.api_views.TypedPagesAPIListingView',
)