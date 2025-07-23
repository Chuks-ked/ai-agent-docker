# Declare what image to use
FROM python:3.13.4-slim-bullseye


# docker build -f Dockerfile -t pyapp .
# docker run -it pyapp


# docker build -f Dockerfile -t chuksked/ai-py-app-test:v1 .
# docker push chuksked/ai-py-app-test:v1

# python -m http.server 8000
# docker run -it -p 3000:8000 pyapp
# docker run -it -p 8000:8000 pyapp
CMD [ "python", "-m", "http.server", "8000" ]
