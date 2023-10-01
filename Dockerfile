
# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Define environment variable
ENV NAME Hospital-Management-System

# Run app.py when the container launches
CMD ["python", "app.py"]
