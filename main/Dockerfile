FROM python:3.11

WORKDIR .

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
