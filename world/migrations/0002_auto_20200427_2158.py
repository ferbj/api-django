# Generated by Django 3.0.5 on 2020-04-28 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
