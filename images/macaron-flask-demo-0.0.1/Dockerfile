# Use the Python 3.10
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the Flask application to listen on
EXPOSE 40080

RUN chmod +x /app/run.sh

# Start the Flask application
CMD ["/app/run.sh"]

