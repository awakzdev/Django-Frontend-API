# Generated by Django 3.1.4 on 2022-06-25 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0013_auto_20220624_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speciality',
            old_name='paradigm',
            new_name='name',
        ),
    ]
