FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY pid/ ./pid/

RUN useradd --create-home --uid 10001 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request,os;urllib.request.urlopen('http://127.0.0.1:'+os.environ.get('PORT','8000')+'/healthz').read()"

# --workers 1 is required: pid/jobs.py holds the job registry in process memory,
# so a poll must land on the same process that started the job.
# --timeout 1800 keeps gunicorn from killing a long extraction thread; client
# requests themselves return in milliseconds.
CMD gunicorn --bind 0.0.0.0:${PORT} --workers 1 --threads 8 \
    --timeout 1800 --graceful-timeout 30 --access-logfile - app:app
