# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 10000 available to the world outside this container
EXPOSE 10000

# Define environment variable to ensure Python output is displayed
ENV PYTHONUNBUFFERED=1

# Run the Gunicorn server with 4 workers, binding to port 10000, and a timeout of 900 seconds
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10000", "--timeout", "900", "-k", "sync", "main:app"]
