from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from pymongo import MongoClient

from insure_brother import settings
from insure_brother.celery import app
from insure_brother.settings import MONGO_INITDB_DATABASE, \
    MONGO_INITDB_USERNAME, MONGO_INITDB_PASSWORD
from main.models import ClientRequest, Insurance


@app.task
def client_request_created(client_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании запроса.
    """
    client_request = ClientRequest.objects.get(pk=client_id)
    insurance = Insurance.objects.get(pk=client_request.insurance_id)
    subject = 'Заявка пользователя на страхование "{}".'.format(insurance.category.category_name)
    context = {'company_name': insurance.company.company_name,
               'category_name': insurance.category.category_name,
               'description': insurance.description,
               'interest_rate': insurance.interest_rate,
               'insurance_amount': insurance.insurance_amount,
               'last_name': client_request.last_name,
               'first_name': client_request.first_name,
               'patronymic': client_request.patronymic,
               'phone': client_request.phone,
               'email': client_request.email}
    html_message = render_to_string(template_name="mails/client_request_created/body.html", context=context)
    txt_message = render_to_string(template_name="mails/client_request_created/body.txt", context=context)

    mail_sent = EmailMultiAlternatives(subject, txt_message, settings.DEFAULT_FROM_EMAIL, [insurance.company.email, ])
    mail_sent.attach_alternative(html_message, "text/html")
    return mail_sent.send(fail_silently=False)


@app.task
def get_mongodb():
    database = MONGO_INITDB_DATABASE
    username = MONGO_INITDB_USERNAME
    password = MONGO_INITDB_PASSWORD
    client = MongoClient(
        host='mongo',
        port=27017,
        serverSelectionTimeoutMS=3000,
        username=username,
        password=password
    )
    # client = MongoClient('mongodb://username_brother:password_brother@mongo')
    db = client[database]
    print('success')
    return db
