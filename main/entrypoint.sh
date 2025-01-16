FROM python:3.9-slim

WORKDIR /main

# Install dependencies
COPY ./requirements.txt /main/requirements.txt
RUN pip install --no-cache-dir -r /main/requirements.txt

# Copy the application code
COPY . /main/

# Expose port 8000 (for the web app)
EXPOSE 8000

# Start the application (example using Gunicorn for Django)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]
