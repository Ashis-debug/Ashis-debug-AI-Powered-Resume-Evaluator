# Use Python 3.12.4 as the base image
FROM python:3.12.4-slim

# Install poppler-utils for PDF processing
RUN apt-get update && apt-get install -y poppler-utils

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask app
ENV FLASK_APP app

# Run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]