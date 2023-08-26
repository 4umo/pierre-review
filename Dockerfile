# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /github/workspace

# Copy the requirements file into the container at /app
COPY requirements.txt /github/workspace/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /github/workspace/

# Set the command to run your main script when the container starts
CMD ["python", "main.py"]