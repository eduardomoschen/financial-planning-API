# Generated by Django 4.2.3 on 2023-10-07 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_transaction_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='budget',
        ),
    ]
