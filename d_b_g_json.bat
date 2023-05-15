py manage.py shell < bp.py
python manage.py dumpdata --natural-foreign --indent 2 ^
    -e contenttypes -e auth.permission ^
    -e wagtailcore.groupcollectionpermission ^
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition ^
    -e wagtailsearch ^
    -e sessions > data.json