# Generated by Django 3.0.7 on 2020-06-24 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200624_0556'),
        ('todo', '0002_todo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo', to='user.User'),
        ),
    ]
