FROM python:3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
&& pip install pipenv mysqlclient

COPY ./Pipfile /usr/src/app/Pipfile

RUN pipenv install --skip-lock --system --dev

COPY . /usr/src/app/
