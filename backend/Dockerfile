# Declare what image to use
FROM python:3.13.4-slim-bullseye

RUN apt-get update && apt-get install -y curl

#create py venvironment
# RUN python -m venv /app/env
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


COPY ./src .

CMD [ "python", "-m", "http.server", "8000" ]
