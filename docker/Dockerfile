FROM python:3.11-slim as base

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements/shared.txt /app/requirements/shared.txt

RUN pip install --no-cache-dir --upgrade pip==23.3.1 \
    && pip install --no-cache-dir -r requirements/shared.txt

FROM base as stt
ENV JOB_ENV=stt
COPY requirements/stt.txt requirements/stt.txt
COPY src/stt src/stt
RUN pip install --no-cache-dir -r requirements/stt.txt
CMD ["python", "src/stt/main.py"]

FROM base as summary
ENV JOB_ENV=stt
COPY src/summary src/summary
COPY requirements/summary.txt requirements/summary.txt
RUN pip install --no-cache-dir -r requirements/summary.txt
CMD ["python", "src/summary/main.py"]
