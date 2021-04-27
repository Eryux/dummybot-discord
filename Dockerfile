# Start with python 3.6 environment
FROM python:3.7-alpine

# Set image informations
LABEL Name=discord_dummy Version=1.1.0 maintainer="C. Nicolas <contact@pawz.xyz>"

# Set workdir
WORKDIR /app

# Add files to app path
COPY . /app

# Install requirements
RUN set -ex \
    && apk --no-cache add --virtual build-dependencies \
        build-base \
        gcc \
        libc-dev \
        libffi-dev \
        python3-dev \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt

# Set entrypoint
ENTRYPOINT ["python3"]

# Run
CMD ["-m", "dummy"]