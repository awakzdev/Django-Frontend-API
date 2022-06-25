# Generated by Django 4.0.4 on 2022-06-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='email',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='comission_pct',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='hire_date',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='manager_id',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='salary',
        ),
        migrations.AddField(
            model_name='worker',
            name='speciality',
            field=models.ManyToManyField(to='workers.speciality'),
        ),
    ]