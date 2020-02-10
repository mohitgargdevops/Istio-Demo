FROM python:3.5-alpine

EXPOSE 8080

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app1-v2.py /usr/src/app/app1-v2.py

CMD [ "python", "app1-v2.py" ]
