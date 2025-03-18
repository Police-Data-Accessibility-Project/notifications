# Dockerfile for the prod-to-dev-migration
FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
# Install dependencies necessary for add-apt-repository
RUN apt-get install software-properties-common -y

# Install Python and pip
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip
# This section ensures that the Python package installation built inside the Dockerfile
# is accessible within the container.
# Set up the working directory
WORKDIR /opt/app

# Copy dependencies and install them
COPY github_data_requests_synchronize/requirements.txt /opt/app/requirements.txt
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt --break-system-packages

# Copy the rest of the application
COPY --chmod=755 helpers /opt/app/helpers
COPY --chmod=755 github_data_requests_synchronize /opt/app/github_data_requests_synchronize

EXPOSE 3000

