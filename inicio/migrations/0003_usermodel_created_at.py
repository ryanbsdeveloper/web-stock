# Generated by Django 4.0.3 on 2022-04-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_usermodel_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
