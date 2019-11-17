# Start with python 3.6 environment
FROM python:3.6-alpine

# Set image informations
LABEL Name=discord_dummy Version=1.0.0 maintainer="C. Nicolas <contact@pawz.xyz>"

# Set workdir
WORKDIR /app

# Add files to app path
COPY . /app

# Install requirements
RUN python3 -m pip install -r requirements.txt

# Set entrypoint
ENTRYPOINT ["python3"]

# Run
CMD ["-m", "dummy"]