py manage.py shell < bp.py
py ./manage.py dumpdata --natural-foreign --indent 2 ^
    -e contenttypes -e auth.permission ^
    -e wagtailcore.groupcollectionpermission ^
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition ^
    -e wagtailcore.pagerevision -e wagtaildocs.documentuserpermission ^

    -e sessions > data.json
git add .
git commit -m "dia %date% hora %time% por %username%"
git push
py manage.py makemigrations
py manage.py migrate
py manage.py loaddata data.json
py manage.py runserver