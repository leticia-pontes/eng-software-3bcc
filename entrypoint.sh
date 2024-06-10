#!/usr/bin/sh -xe

echo "Applying database migrations..."
python manage.py migrate

echo "Starting server..."
exec "$@"
