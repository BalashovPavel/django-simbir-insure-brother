FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/app
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .

#docker-compose run web python manage.py migrate
#docker-compose run web python manage.py makemigrations
