# Generated by Django 3.2.8 on 2021-10-11 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('name_app', '0013_auto_20211008_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='username',
        ),
    ]
