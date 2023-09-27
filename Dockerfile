FROM python:3.9.18-slim-bullseye

#Testing Dockerfile
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3","-u", "run.py"]






#RUN apt-get update && \
#    apt-get upgrade -y && \
#    apt-get install -y git

#RUN git clone https://github.com/Cavi421/Connect4 /app

#WORKDIR /app
#ENTRYPOINT ["python3","-u", "run.py"]