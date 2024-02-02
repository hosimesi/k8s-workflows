FROM python:3.11-slim as base


RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements/shared.txt /app/requirements/shared.txt
# COPY jobs/models /app/jobs/models
# COPY jobs/shared /app/jobs/shared
# COPY jobs/artifacts /app/jobs/artifacts
COPY jobs/models /app/models
COPY jobs/shared /app/shared
COPY jobs/artifacts /app/artifacts

RUN pip install --no-cache-dir --upgrade pip==23.3.1 \
    && pip install --no-cache-dir -r requirements/shared.txt

FROM base as entrypoint
ENV JOB_ENV=entrypoint
COPY jobs/tasks/entrypoint .
# COPY requirements/entrypoint.txt requirements/entrypoint.txt
# RUN pip install --no-cache-dir -r requirements/entrypoint.txt
CMD ["python", "main.py"]

FROM base as vad
ENV JOB_ENV=vad
# COPY requirements/vad.txt requirements/vad.txt
COPY jobs/tasks/vad .
# RUN pip install --no-cache-dir -r requirements/vad.txt
CMD ["python", "main.py"]

FROM base as stt
ENV JOB_ENV=stt
COPY requirements/stt.txt requirements/stt.txt
COPY jobs/tasks/stt .
RUN pip install --no-cache-dir -r requirements/stt.txt
CMD ["python", "main.py"]

FROM base as summary
ENV JOB_ENV=summary
COPY requirements/summary.txt requirements/summary.txt
COPY jobs/tasks/summary .
RUN pip install --no-cache-dir -r requirements/summary.txt
CMD ["python", "main.py"]


FROM base as aggregate
ENV JOB_ENV=aggregate
# COPY requirements/aggregate.txt requirements/aggregate.txt
COPY jobs/tasks/aggregate .
# RUN pip install --no-cache-dir -r requirements/aggregate.txt
CMD ["python", "main.py"]
