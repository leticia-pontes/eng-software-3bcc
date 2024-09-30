#!/bin/bash
set -e

echo "Applying database migrations..."
python manage.py migrate

python palavra/criar_dicionario.py

echo "Starting server..."
exec "$@"
