py manage.py shell < bp.py
py ./manage.py dumpdata --natural-foreign --indent 2 -e auth.permission -e contenttypes -e wagtailcore.GroupCollectionPermission -e wagtailcore.revision -e wagtailimages.rendition -e sessions -e wagtailsearch.indexentry -e wagtailsearch.sqliteftsindexentry -e wagtailcore.referenceindex -e wagtailcore.pagesubscription -e wagtailcore.modellogentry -e wagtailcore.pagelogentry > bakerydemo.json
prettier --write bakerydemo.json




python manage.py dumpdata --natural-foreign --indent 2  -e contenttypes -e auth.permission -e wagtailcore.groupcollectionpermission  -e wagtailcore.grouppagepermission -e wagtailimages.rendition  -e wagtailsearch.indexentry -e wagtailsearch.sqliteftsindexentry  -e sessions > data.json