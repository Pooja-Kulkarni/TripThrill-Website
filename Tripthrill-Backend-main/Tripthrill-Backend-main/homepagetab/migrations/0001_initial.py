# Generated by Django 3.1.2 on 2021-08-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PropertyTypeName', models.TextField(max_length=200)),
            ],
        ),
    ]
