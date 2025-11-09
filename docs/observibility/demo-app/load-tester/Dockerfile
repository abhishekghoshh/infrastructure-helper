# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the load testing script into the container
COPY load_tester.py ./

# Set the entrypoint for the container to run the script
CMD ["python", "load_tester.py"]
