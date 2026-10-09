FROM python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/BMerrick18/Dental-Ben"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]