FROM python:3.9.18-slim-bullseye

#Unit-tests Dockerfile
#To run tests uncomment here
#COPY . /app
#WORKDIR /app
#CMD ["python3", "-m", "unittest", "discover", "-b"]



#Development Dockerfile and Final Version. Leave this one uncommented
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3","-u", "run.py"]



#### This one gave me problems with dockerignore
#RUN apt-get update && \
#    apt-get upgrade -y && \
#    apt-get install -y git

#RUN git clone https://github.com/Cavi421/Connect4 /app

#WORKDIR /app
#ENTRYPOINT ["python3","-u", "run.py"]