# Generated by Django 3.1.4 on 2022-06-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0004_auto_20220618_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='workers',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='paradigm',
            old_name='speciality',
            new_name='jobs',
        ),
        migrations.RemoveField(
            model_name='job',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='paradigm',
        ),
        migrations.AddField(
            model_name='job',
            name='speciality',
            field=models.ManyToManyField(to='workers.Paradigm'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='commission_pct',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.RemoveField(
            model_name='worker',
            name='job_id',
        ),
        migrations.AddField(
            model_name='worker',
            name='job_id',
            field=models.ManyToManyField(to='workers.Paradigm'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='manager_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
