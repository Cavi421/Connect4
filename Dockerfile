FROM python:3.9.18-slim-bullseye
#FROM python:3.9.18-bullseye

#Unit-tests Dockerfile
#COPY . /app
#WORKDIR /app
#CMD ["python3", "-m", "unittest", "discover", "-b"]



#Development Dockerfile
#COPY . /app
#WORKDIR /app
#ENTRYPOINT ["python3","-u", "run.py"]





#### Final Version that download the code from Github and executes it
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN git clone https://github.com/Cavi421/Connect4 /app

WORKDIR /app
ENTRYPOINT ["python3","-u", "run.py"]