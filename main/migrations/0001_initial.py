# Generated by Django 3.2 on 2021-07-23 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
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
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150, verbose_name='Краткое описание')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Процентная ставка')),
                ('insurance_amount', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Страховая сумма')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Тип страхования')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance', to='user.companyprofile', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Страховое предложение',
                'verbose_name_plural': 'Страховые предложения',
            },
        ),
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.insurance', verbose_name='Страховое предложение')),
            ],
            options={
                'verbose_name': 'Заявка клиента',
                'verbose_name_plural': 'Заявки клиентов',
            },
        ),
    ]