FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY src/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ /app/

# Port environment variable
ENV PORT=8080

# Run collectstatic (will be served by whitenoise)
RUN python manage.py collectstatic --noinput

# Run the app with gunicorn
CMD exec gunicorn MyPortfolio.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0
