FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD . /usr/src/app

EXPOSE 5000

CMD ["python2", "./server.py"]