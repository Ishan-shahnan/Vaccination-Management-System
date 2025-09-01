#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Building the project..."

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files
# This command gathers all static files (CSS, JS, images) into a single directory.
python manage.py collectstatic --noinput

# 3. Apply database migrations
# This command updates your database schema with the latest changes from your models.
python manage.py migrate

echo "Build finished."