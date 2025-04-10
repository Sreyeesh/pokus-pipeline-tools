FROM python:3.12-alpine

# 🌱 Environment setup
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VENV_PATH=/venv \
    PATH="/venv/bin:$PATH"

# 🧰 Install system dependencies & create Python venv
RUN apk update && apk add --no-cache \
    bash \
    git \
    ffmpeg \
    sqlite \
    python3-dev \
    build-base \
    libffi-dev \
    openssl-dev \
    musl-dev \
    && python3 -m venv $VENV_PATH

# 📦 Install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# 📁 Copy entrypoint script into container
COPY docker/entrypoint.sh /studio/docker/entrypoint.sh

# 🧼 Make sure entrypoint is executable
RUN chmod +x /studio/docker/entrypoint.sh

# 📂 Set working directory
WORKDIR /studio

# 🚀 Default command
ENTRYPOINT ["/studio/docker/entrypoint.sh"]
