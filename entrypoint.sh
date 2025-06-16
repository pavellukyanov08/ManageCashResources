#!/bin/bash

set -e

echo "🔁 Applying migrations..."
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  echo "👤 Checking if superuser $DJANGO_SUPERUSER_USERNAME exists..."
  python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
username = '$DJANGO_SUPERUSER_USERNAME'
if not User.objects.filter(username=username).exists():
    print('✅ Superuser does not exist, creating...')
    User.objects.create_superuser(
        username=username,
        email='$DJANGO_SUPERUSER_EMAIL',
        password='$DJANGO_SUPERUSER_PASSWORD'
    )
else:
    print('Superuser already exists.')
" || echo "Superuser creation failed, but continuing..."
fi


echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "🚀 Starting Gunicorn..."
exec gunicorn cashflow_app.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --log-level=info \
  --access-logfile=/var/log/gunicorn/access.log \
  --error-logfile=/var/log/gunicorn/error.log