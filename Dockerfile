FROM python:3.10-alpine

WORKDIR /Code

COPY . .

RUN pip install -r requirements.txt

CMD python3 app