FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VENV_PATH=/venv \
    PATH="/venv/bin:$PATH"

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

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

WORKDIR /studio

ENTRYPOINT ["bash"]
