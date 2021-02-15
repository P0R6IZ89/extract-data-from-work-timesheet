FROM python:3.8.7-alpine3.13
WORKDIR /app
RUN apk update 
RUN apk add firefox 
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz 
RUN tar -zxf geckodriver-v0.29.0-linux64.tar.gz -C /usr/bin 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python3", "./app.py"]