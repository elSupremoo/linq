FROM python:3.13.3-slim-bookworm

WORKDIR /app

COPY . /app

RUN pip install pymongo matplotlib

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]