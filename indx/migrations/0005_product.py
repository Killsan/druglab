# Generated by Django 3.0.8 on 2020-08-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('indx', '0004_delete_app_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_cost', models.CharField(max_length=10)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_img', models.FileField(upload_to='')),
            ],
        ),
    ]
