# ===== Stage 1: builder =====
FROM python:3.11-slim AS builder

ENV PIP_NO_CACHE_DIR=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Install dependencies required for venv and package builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

# Copy requirements
COPY requirements.txt .

# Create virtual environment + install dependencies
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt


# ===== Stage 2: runtime =====
FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PATH="/opt/venv/bin:$PATH"

# Create non-root user
RUN addgroup --system app && adduser --system --ingroup app app

WORKDIR /app
RUN chown -R app:app /app

# Copy installed virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY --chown=app:app app.py /app/app.py

USER app

EXPOSE 8080

# Start the service with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "2", "app:app"]
