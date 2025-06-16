#!/bin/bash

# Применение миграций
python manage.py migrate

# Создание суперпользователя (если не существует)
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL || true
fi

# Сбор статики
python manage.py collectstatic --noinput --clear

# Запуск Gunicorn
exec gunicorn ManageCashResources.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --log-level=info \
  --access-logfile=/var/log/gunicorn/access.log \
  --error-logfile=/var/log/gunicorn/error.log