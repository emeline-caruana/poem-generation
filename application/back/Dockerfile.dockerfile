# Use an official Python image with Python 3.10
FROM python:3.10-slim

# Meta-data
LABEL version="1.0"
LABEL maintainer="Emeline Caruana"

# Update pip
RUN python3 -m pip install --no-cache-dir --upgrade pip

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY ./back/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files into the container
COPY ./back /app

# Expose the port the application will use
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Define the command to run the application when the container starts
CMD ["python", "app.py"]
