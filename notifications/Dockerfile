# Dockerfile for the prod-to-dev-migration
FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
# Install dependencies necessary for add-apt-repository
RUN apt-get install software-properties-common -y
RUN apt-get -y update && apt-get -y install curl


# Install Python and pip
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip
# This section ensures that the Python package installation built inside the Dockerfile
# is accessible within the container.
COPY notifications/requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt --break-system-packages
COPY . /opt/app

# Copy the app folder into the image
COPY --chmod=755 helpers /opt/app/helpers
COPY --chmod=755 notifications /opt/app/notifications

EXPOSE 3000
