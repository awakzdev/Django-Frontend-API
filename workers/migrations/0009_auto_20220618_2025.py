# Generated by Django 3.1.4 on 2022-06-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0008_auto_20220618_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
