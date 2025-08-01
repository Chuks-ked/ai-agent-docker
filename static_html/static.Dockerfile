# Declare what image to use
FROM python:3.13.4-slim-bullseye

WORKDIR /app


# COPY loal_folder container_folder
# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

# Same destination folder is /app 
# COPY ./static_html /app
COPY ./src .

# RUN echo "hello world" > index.html

# docker build -f Dockerfile -t pyapp .
# docker run -it pyapp


# docker build -f Dockerfile -t chuksked/ai-py-app-test:v1 .
# docker push chuksked/ai-py-app-test:v1

# python -m http.server 8000
# docker run -it -p 3000:8000 pyapp
# docker run -it -p 8000:8000 pyapp
CMD [ "python", "-m", "http.server", "8000" ]
