# Generated by Django 3.1 on 2020-08-28 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indx', '0010_bot_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='date',
        ),
    ]
