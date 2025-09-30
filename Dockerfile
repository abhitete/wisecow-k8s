# Use Ubuntu as base image
FROM ubuntu:20.04

# Avoid interactive prompts (like timezone selection) during build
ENV DEBIAN_FRONTEND=noninteractive

# Add /usr/games to PATH (where fortune + cowsay live)
ENV PATH="/usr/games:${PATH}"

# Install required packages: fortune, cowsay, netcat
RUN apt-get update && apt-get install -y \
    fortune-mod \
    cowsay \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy the wisecow script into the container
COPY wisecow.sh .

# Fix Windows line endings (CRLF -> LF) and make script executable
RUN sed -i 's/\r$//' wisecow.sh && chmod +x wisecow.sh

# Expose Wisecow port
EXPOSE 4499

# Run the script when the container starts
CMD ["./wisecow.sh"]
