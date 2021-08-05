from django.core.mail import EmailMessage

from insure_brother import settings
from insure_brother.celery import app
from main.models import ClientRequest, Insurance


@app.task
def client_request_created(client_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании запроса.
    """
    client_request = ClientRequest.objects.get(pk=client_id)
    insurance = Insurance.objects.get(pk=client_request.insurance_id)
    subject = 'Заявка пользователя на страхование "{}".'.format(insurance.category.category_name)
    message = '{}, вам пришла заявка на получение услуги страхования "{}".\n\n' \
              'Описание услуги срахования:\nКомпания: {}\nТип страхования: {}\n' \
              'Краткое описание: {}\nПроцентная ставка: {}%\nСтраховая сумма: {}руб.\n\n' \
              'Информация о пользователе:\nФИО: {} {} {}\nТелефон: {}\nEmail: {}.'.format(
                insurance.company.company_name, insurance.category.category_name,
                insurance.company.company_name, insurance.category.category_name,
                insurance.description, insurance.interest_rate, insurance.insurance_amount,
                client_request.last_name, client_request.first_name, client_request.patronymic,
                client_request.phone, client_request.email
              )

    mail_sent = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [insurance.company.email, ])

    return mail_sent.send(fail_silently=False)
