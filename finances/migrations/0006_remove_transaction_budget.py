# Generated by Django 4.2.4 on 2023-10-07 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_transaction_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='budget',
        ),
    ]
