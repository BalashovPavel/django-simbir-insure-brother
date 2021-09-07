from django.contrib.auth.models import User
from django.db import models

from user.models import CompanyProfile


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Тип страхования')
    slug = models.SlugField(null=False, unique=True, verbose_name='Ключ')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Тип страхования'
        verbose_name_plural = 'Типы страхования'


class Insurance(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='insurance',
                                verbose_name='Компания', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Тип страхования', null=True)
    description = models.CharField(max_length=150, verbose_name='Краткое описание')
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процентная ставка')
    insurance_amount = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Страховая сумма')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        insurance_title = self.category.category_name + "/" + self.company.company_name
        return insurance_title

    class Meta:
        verbose_name = 'Страховое предложение'
        verbose_name_plural = 'Страховые предложения'


class ClientRequest(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, verbose_name='Страховое предложение')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(max_length=150, verbose_name='Email')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Заявка клиента'
        verbose_name_plural = 'Заявки клиентов'
