# Generated by Django 4.0.3 on 2022-05-07 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_remove_usermodel_created_at_usermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
