# Generated by Django 3.1.4 on 2022-06-24 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0012_auto_20220624_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='hire_date',
            field=models.DateField(),
        ),
    ]
