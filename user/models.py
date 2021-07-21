from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин')
    company_name = models.CharField(max_length=150, verbose_name='Название компании')
    email = models.CharField(max_length=150, verbose_name='Email')
    address = models.CharField(max_length=150, verbose_name='Юридический адрес')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Профиль компании'
        verbose_name_plural = 'Профили компаний'
