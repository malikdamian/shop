# Generated by Django 3.2.7 on 2021-09-22 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('name_app', '0002_alter_product_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='image',
        ),
    ]