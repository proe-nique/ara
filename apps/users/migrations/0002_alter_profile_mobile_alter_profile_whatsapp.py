# Generated by Django 4.1.1 on 2022-09-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(default='+263 000 000 000'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='whatsapp',
            field=models.IntegerField(default='+263 000 000 000'),
        ),
    ]
