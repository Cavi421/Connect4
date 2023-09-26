FROM python:3.9.18-slim-bullseye

RUN pip install numpy

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3","-u", "run.py"]