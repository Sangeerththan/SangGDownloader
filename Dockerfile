FROM python:3

COPY Downloader Downloader/
RUN pwd
RUN cd .. \
    pip install -r requirements.txt

CMD [ "python", "main.py" ]