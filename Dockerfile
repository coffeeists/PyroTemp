FROM python:3.10-alpine

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD python3 .