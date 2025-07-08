# Use an official Python base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Hugging Face expects
EXPOSE 7860

# Run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "main:server"]