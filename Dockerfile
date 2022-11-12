FROM python:3.10-bullseye

WORKDIR /home/python/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y \
  && apt install gcc python3-dev musl-dev bash build-essential libssl-dev libffi-dev -y

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /home/python/app/entrypoint.sh
RUN chmod +x /home/python/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/home/python/app/entrypoint.sh"]
