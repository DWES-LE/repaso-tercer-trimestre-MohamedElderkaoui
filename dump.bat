
python manage.py dumpdata --natural-foreign --indent 2 ^
    -e contenttypes -e auth.permission ^
    -e wagtailcore.groupcollectionpermission ^
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition ^
    -e sessions > data.json
py manage.py shell < bp.py
PY manage.py  makemigrations
PY manage.py  migrate
PY manage.py  loaddata data.json
PY manage.py  runserver