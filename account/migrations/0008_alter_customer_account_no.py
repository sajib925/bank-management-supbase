# Generated by Django 5.0.6 on 2024-09-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_customer_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_no',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
