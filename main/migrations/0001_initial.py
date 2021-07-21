# Generated by Django 3.2.5 on 2021-07-18 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Тип страхования')),
                ('slug', models.SlugField(unique=True, verbose_name='Ключ')),
            ],
            options={
                'verbose_name': 'Тип страхования',
                'verbose_name_plural': 'Типы страхования',
            },
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('insurance_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Тип страхования')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance', to='main.companyprofile', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Тип страхования',
                'verbose_name_plural': 'Типы страхования',
            },
        ),
    ]