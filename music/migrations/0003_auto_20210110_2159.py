# Generated by Django 3.1.4 on 2021-01-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210110_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='len',
            field=models.FloatField(),
        ),
    ]
