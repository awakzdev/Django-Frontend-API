# Generated by Django 4.0.4 on 2022-06-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_worker_commission_pct_worker_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='speciality',
            field=models.ManyToManyField(blank=True, to='workers.speciality'),
        ),
    ]