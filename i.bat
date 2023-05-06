for app in $(python manage.py showmigrations --list | grep '^[a-z]' | cut -d' ' -f1); do python manage.py sqlmigrate $app 0001 >> all_migrations.sql; done
