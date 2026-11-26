FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 \
    PATH="/usr/lib/jvm/java-17-openjdk-amd64/bin:${PATH}" \
    PYSPARK_PYTHON=python3 \
    PYSPARK_DRIVER_PYTHON=python3

RUN apt-get update \
    && apt-get install -y --no-install-recommends openjdk-17-jre-headless procps curl ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8888

CMD ["bash", "-lc", "jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.token=${JUPYTER_TOKEN:-change-this-token}"]
