# Generated by Django 3.0.7 on 2020-07-01 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20200701_0933'),
        ('user', '0003_auto_20200624_0625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
