
# Use official Python 3.11 image as base
FROM python:3.11

# Set working directory inside the container
WORKDIR /playwright

# Copy all project files from host to container
COPY . .

# Install Python dependencies listed in requirements.txt
# --no-cache-dir avoids caching pip packages to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and necessary dependencies
# Ensures Chromium, Firefox, WebKit work properly inside container
RUN playwright install --with-deps

# Default command to run when container starts
CMD ["pytest", "-v", "-s"]