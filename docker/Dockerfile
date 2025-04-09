# 🧼 Secure, minimal Alpine base image with Python 3.12
FROM python:3.12-alpine

# 🔧 Environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VENV_PATH=/venv \
    PATH="/venv/bin:$PATH"

# 🧰 Install system dependencies and build tools
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

# 📦 Install Python packages inside venv
COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# 📂 Set workdir
WORKDIR /studio

# ✅ JSON-style ENTRYPOINT
ENTRYPOINT ["bash"]
