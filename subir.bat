py manage.py shell < bp.py
python manage.py dumpdata --natural-foreign --indent 2 ^
    -e contenttypes -e auth.permission ^
    -e wagtailcore.groupcollectionpermission ^
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition ^
    -e wagtailsearch ^
    -e sessions > data.json
git add .
git commit -m "fecha: %date% hora: %time% por: %username% que a traido: %1"
git push
py manage.py makemigrations
py manage.py migrate
py manage.py  loaddata data.json 
py manage.py runserver
