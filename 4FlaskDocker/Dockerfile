ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

WORKDIR /home/flask
COPY requirements.txt /tmp/pip-tmp/
COPY app.py .
COPY data/ .
COPY templates/ .

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

CMD python app.py
 