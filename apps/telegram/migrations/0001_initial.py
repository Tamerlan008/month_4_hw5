# Generated by Django 5.0.6 on 2024-07-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('persone', models.CharField(choices=[('1 - Persone', '1 - Persone'), ('2 - Persone', '2 - Persone'), ('3 - Persone', '3 - Persone'), ('4 - Persone', '4 - Persone'), ('5 - Persone', '5 - Persone')], max_length=20, verbose_name='Количество людей')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.CharField(choices=[('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('12:00 AM', '12:00 AM'), ('1:00 AM', '1:00 AM'), ('2:00 AM', '2:00 AM'), ('3:00 AM', '3:00 AM')], max_length=20, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Резервация',
                'verbose_name_plural': 'Резервации',
            },
        ),
    ]
