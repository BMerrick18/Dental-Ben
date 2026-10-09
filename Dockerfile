FROM python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/BMerrick18/Dental-Ben"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# The app writes its SQLite database into /app, so this user must own that folder.
RUN useradd --create-home --uid 10001 appuser \
    && chown appuser:appuser /app

COPY requirements.txt .
# The Python base image ships an old setuptools. Replace it before installing the app.
RUN pip install --no-cache-dir "setuptools==84.0.0" "wheel==0.48.0" \
    && pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

USER 10001

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
