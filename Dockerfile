FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
COPY Downloader Downloader/
ADD main.py requirements.txt /
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN export DISPLAY=:0.0
RUN apt-get install python3-tk
CMD [ "python", "main.py" ]