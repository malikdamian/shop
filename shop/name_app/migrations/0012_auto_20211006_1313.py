# Generated by Django 3.2.7 on 2021-10-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name_app', '0011_auto_20211006_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
