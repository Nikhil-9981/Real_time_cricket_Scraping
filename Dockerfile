# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    chromium \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the environment variable for Chrome binary location
ENV CHROME_BIN=/usr/bin/chromium

# Install chromedriver
RUN curl -sSL https://chromedriver.storage.googleapis.com/$(curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip -o /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

# Set the environment variable for ChromeDriver binary location
ENV PATH=$PATH:/usr/local/bin/

# Create a directory for the app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
